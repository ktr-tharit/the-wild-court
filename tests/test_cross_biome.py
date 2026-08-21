import json
import unittest
from pathlib import Path

from scripts.simulate_cross_biome import build_report, load_model, model_errors
from scripts.render_desert_boundary_bank import OUTPUT as BOUNDARY_DOC
from scripts.render_desert_boundary_bank import render as render_boundary_bank
from scripts.validate_question_evidence import (
    evidence_errors,
    load_example,
    motive_domain_coverage,
)


ROOT = Path(__file__).resolve().parents[1]
BOUNDARY_BANK = ROOT / "data" / "desert-taiga-boundary-bank.v0.1.json"
BOUNDARY_BANK_V02 = ROOT / "data" / "desert-taiga-boundary-bank.v0.2.json"
DESERT_BIBLE_DIR = ROOT / "docs" / "design" / "animals" / "desert"


class CrossBiomeSandboxTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = load_model()
        cls.report = build_report(cls.model)

    def test_anchor_model_schema(self):
        self.assertEqual(model_errors(self.model), [])

    def test_question_evidence_example(self):
        self.assertEqual(evidence_errors(load_example()), [])

    def test_desert_taiga_boundary_bank_schema(self):
        bank = json.loads(BOUNDARY_BANK.read_text(encoding="utf-8"))
        self.assertEqual(evidence_errors(bank), [])
        extension = json.loads(BOUNDARY_BANK_V02.read_text(encoding="utf-8"))
        self.assertEqual(evidence_errors(extension), [])

    def test_v02_collision_clusters_have_two_independent_items(self):
        base = json.loads(BOUNDARY_BANK.read_text(encoding="utf-8"))
        extension = json.loads(BOUNDARY_BANK_V02.read_text(encoding="utf-8"))
        questions = base["questions"] + extension["questions"]
        pair_clusters = [
            {"Lynx", "Caracal"},
            {"Reindeer", "Oryx"},
            {"Scorpion", "Moose"},
            {"Scorpion", "Caracal"},
            {"Cobra", "Moose"},
        ]
        for cluster in pair_clusters:
            matching = [
                question for question in questions
                if cluster.issubset(set(question["discriminates"]))
            ]
            with self.subTest(cluster=sorted(cluster)):
                self.assertGreaterEqual(len(matching), 2)
                self.assertGreaterEqual(len({item["domain"] for item in matching}), 2)
        camel_cluster = [
            question for question in questions
            if "Camel" in question["discriminates"]
            and ({"Reindeer", "Bear"} & set(question["discriminates"]))
        ]
        self.assertGreaterEqual(len(camel_cluster), 2)
        self.assertGreaterEqual(len({item["domain"] for item in camel_cluster}), 2)

    def test_desert_taiga_bank_covers_every_desert_anchor(self):
        bank = json.loads(BOUNDARY_BANK.read_text(encoding="utf-8"))
        desert_animals = {
            "Fennec Fox", "Caracal", "Cobra", "Camel", "Scorpion", "Oryx"
        }
        covered = {
            animal
            for question in bank["questions"]
            for animal in question["discriminates"]
        }
        self.assertTrue(desert_animals.issubset(covered))

    def test_motive_probes_span_three_domains(self):
        bank = json.loads(BOUNDARY_BANK.read_text(encoding="utf-8"))
        domains = set().union(*motive_domain_coverage(bank).values())
        self.assertGreaterEqual(len(domains), 3)

    def test_rendered_boundary_bank_is_current(self):
        self.assertEqual(
            BOUNDARY_DOC.read_text(encoding="utf-8"), render_boundary_bank()
        )

    def test_all_desert_animal_bibles_are_complete(self):
        expected = {
            "fennec-fox.md", "caracal.md", "cobra.md",
            "camel.md", "scorpion.md", "oryx.md",
        }
        self.assertEqual({path.name for path in DESERT_BIBLE_DIR.glob("*.md")}, expected)
        required_sections = {
            "## Identity",
            "## Psychology",
            "## Kingdom fit",
            "## Provisional trait rationale",
            "## Distinctions",
            "## Scenario anchors",
            "## Adaptive tie-breaker seeds",
            "## Visual direction",
            "## Result-page draft",
        }
        for path in DESERT_BIBLE_DIR.glob("*.md"):
            content = path.read_text(encoding="utf-8")
            with self.subTest(animal=path.stem):
                self.assertTrue(required_sections.issubset(set(content.splitlines())))
                self.assertEqual(content.count("| AFF |"), 1)
                self.assertEqual(content.count("| ALG |"), 1)
                self.assertIn("**Share line:**", content)

    def test_facets_do_not_reduce_overall_recovery(self):
        self.assertGreaterEqual(self.report["simulation"]["overall_lift"], 0.0)

    def test_facets_improve_critical_cluster_recovery(self):
        self.assertGreater(
            self.report["simulation"]["critical_cluster_lift"], 0.0
        )


if __name__ == "__main__":
    unittest.main()
