import unittest
from pathlib import Path

from scripts.simulate_taiga_desert import (
    build_report,
    estimate_constructs,
    load_json,
    model_errors,
    normalized_priors,
    softmax_scores,
    DEFAULT_MODEL,
)


class TaigaDesertWeightedSoftmaxTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = load_json(DEFAULT_MODEL)
        cls.report = build_report(cls.model)

    def test_model_schema(self):
        self.assertEqual(model_errors(self.model), [])

    def test_priors_are_normalized_across_realms_and_animals(self):
        priors = normalized_priors(self.model)
        self.assertAlmostEqual(sum(priors.values()), 1.0)
        taiga = sum(
            prior for name, prior in priors.items()
            if self.model["animals"][name]["realm"] == "Taiga"
        )
        self.assertAlmostEqual(taiga, 0.5)

    def test_weighted_estimate_respects_evidence_strength(self):
        responses = [{
            "evidence": [
                {"construct": "AFF", "value": 1.0, "weight": 1.0},
                {"construct": "AGY", "value": 0.0, "weight": 1.0},
            ]
        }, {
            "evidence": [
                {"construct": "AFF", "value": -1.0, "weight": 0.5},
                {"construct": "AGY", "value": 0.0, "weight": 1.0},
            ]
        }]
        estimates, _ = estimate_constructs(
            responses, self.model, include_facets=False
        )
        self.assertAlmostEqual(estimates["AFF"], 1.0 / 3.0)

    def test_softmax_probabilities_and_realm_sums_are_normalized(self):
        estimates = {construct: 0.0 for construct in self.model["core_dimensions"]}
        confidence = {construct: 1.0 for construct in estimates}
        result = softmax_scores(estimates, confidence, self.model)
        self.assertAlmostEqual(sum(result["animal_probabilities"].values()), 1.0)
        self.assertAlmostEqual(sum(result["realm_probabilities"].values()), 1.0)

    def test_desert_bible_scores_match_canonical_model(self):
        root = Path(__file__).resolve().parents[1]
        bible_dir = root / "docs" / "design" / "animals" / "desert"
        files = {
            "Fennec Fox": "fennec-fox.md",
            "Caracal": "caracal.md",
            "Cobra": "cobra.md",
            "Camel": "camel.md",
            "Scorpion": "scorpion.md",
            "Oryx": "oryx.md",
        }
        for animal, filename in files.items():
            content = (bible_dir / filename).read_text(encoding="utf-8").splitlines()
            scores = {}
            for line in content:
                cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                if len(cells) >= 2 and cells[0] in self.model["core_dimensions"]:
                    scores[cells[0]] = float(cells[1])
            with self.subTest(animal=animal):
                expected = dict(zip(
                    self.model["core_dimensions"],
                    self.model["animals"][animal]["core"],
                ))
                self.assertEqual(scores, expected)

    def test_selected_weighted_softmax_model_beats_core_baseline(self):
        baseline = self.report["modes"]["core_softmax"]
        selected = self.report["modes"][self.report["selected_mode"]]
        self.assertGreater(selected["animal_accuracy"], baseline["animal_accuracy"])
        self.assertGreaterEqual(selected["realm_accuracy"], baseline["realm_accuracy"])

    def test_adaptive_question_budget_is_bounded(self):
        selected = self.report["modes"][self.report["selected_mode"]]
        self.assertLessEqual(selected["average_extra_questions"], 2.0)


if __name__ == "__main__":
    unittest.main()
