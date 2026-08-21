import unittest

from scripts.simulate_cross_biome import build_report, load_model, model_errors
from scripts.validate_question_evidence import evidence_errors, load_example


class CrossBiomeSandboxTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = load_model()
        cls.report = build_report(cls.model)

    def test_anchor_model_schema(self):
        self.assertEqual(model_errors(self.model), [])

    def test_question_evidence_example(self):
        self.assertEqual(evidence_errors(load_example()), [])

    def test_facets_do_not_reduce_overall_recovery(self):
        self.assertGreaterEqual(self.report["simulation"]["overall_lift"], 0.0)

    def test_facets_improve_critical_cluster_recovery(self):
        self.assertGreater(
            self.report["simulation"]["critical_cluster_lift"], 0.0
        )


if __name__ == "__main__":
    unittest.main()
