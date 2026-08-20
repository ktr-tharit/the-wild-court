import unittest

from scripts.simulate_questions import (
    bank_errors,
    coverage,
    domain_distribution,
    load_bank,
    simulate,
)
from scripts.validate_vectors import load_model


class QuestionBankV01Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bank = load_bank()
        cls.model = load_model()
        cls.simulation = simulate(cls.bank, cls.model)

    def test_schema(self):
        self.assertEqual(bank_errors(self.bank, self.model), [])

    def test_each_trait_is_measured_four_times(self):
        self.assertEqual(set(coverage(self.bank, self.model).values()), {4})

    def test_public_power_is_not_the_majority_domain(self):
        domains = domain_distribution(self.bank)
        share = domains.get("public_power", 0) / len(self.bank["questions"])
        self.assertLessEqual(share, 0.30)

    def test_question_simulation_reaches_accuracy_target(self):
        self.assertGreaterEqual(self.simulation["accuracy"], 0.80)

    def test_every_animal_reaches_accuracy_floor(self):
        self.assertGreaterEqual(
            min(self.simulation["per_animal_accuracy"].values()), 0.75
        )

    def test_vector_estimation_error_is_bounded(self):
        self.assertLessEqual(self.simulation["mean_absolute_error"], 0.35)


if __name__ == "__main__":
    unittest.main()

