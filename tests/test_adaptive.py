import unittest

from scripts.simulate_adaptive import (
    adaptive_bank_errors,
    load_adaptive_bank,
    simulate_adaptive,
)
from scripts.simulate_questions import load_bank
from scripts.validate_vectors import load_model


class AdaptiveQuestionBankV01Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.core_bank = load_bank()
        cls.adaptive_bank = load_adaptive_bank()
        cls.model = load_model()
        cls.result = simulate_adaptive(cls.core_bank, cls.adaptive_bank, cls.model)

    def test_schema_and_pair_coverage(self):
        self.assertEqual(adaptive_bank_errors(self.adaptive_bank, self.model), [])

    def test_adaptive_questions_improve_overall_accuracy(self):
        self.assertGreaterEqual(self.result["accuracy_lift"], 0.01)

    def test_each_ambiguity_cluster_animal_improves(self):
        for animal in ("Grey Wolf", "Bear", "Moose"):
            self.assertGreater(self.result["per_animal_lift"][animal], 0)

    def test_average_question_budget_stays_below_one(self):
        self.assertLessEqual(self.result["average_extra_questions"], 1.0)

    def test_final_accuracy_reaches_target(self):
        self.assertGreaterEqual(self.result["adaptive_accuracy"], 0.88)


if __name__ == "__main__":
    unittest.main()

