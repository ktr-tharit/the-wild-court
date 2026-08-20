import unittest

from scripts.validate_vectors import (
    dimension_spans,
    load_model,
    pairwise_distances,
    recovery_simulation,
    schema_errors,
)


class VectorModelV03Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = load_model()
        cls.thresholds = cls.model["validation_thresholds"]
        cls.animals = {
            name: item["vector"] for name, item in cls.model["animals"].items()
        }

    def test_schema_and_ranges(self):
        self.assertEqual(schema_errors(self.model), [])

    def test_taiga_animals_have_minimum_separation(self):
        closest = pairwise_distances(self.animals)[0]
        self.assertGreaterEqual(closest[0], self.thresholds["minimum_animal_distance"])

    def test_each_dimension_has_useful_span(self):
        spans = dimension_spans(self.model)
        self.assertGreaterEqual(min(spans.values()), self.thresholds["minimum_dimension_span"])

    def test_no_animal_vectors_are_identical(self):
        distances = pairwise_distances(self.animals)
        self.assertTrue(all(distance > 0 for distance, _, _ in distances))

    def test_prototypes_recover_under_moderate_noise(self):
        result = recovery_simulation(self.model)
        self.assertGreaterEqual(
            result["accuracy"], self.thresholds["minimum_recovery_accuracy"]
        )

    @unittest.expectedFailure
    def test_provisional_kingdom_fingerprints_are_separated(self):
        """Known design issue: Taiga and Desert are too close in v0.3."""
        closest = pairwise_distances(self.model["kingdom_fingerprints"])[0]
        self.assertGreaterEqual(closest[0], self.thresholds["minimum_kingdom_distance"])


if __name__ == "__main__":
    unittest.main()

