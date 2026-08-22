import unittest

from scripts.export_web_bundle import DEFAULT_OUTPUT, build_bundle, render_bundle


class WebBundleV01Tests(unittest.TestCase):
    def test_bundle_contains_complete_three_realm_runtime(self):
        bundle = build_bundle()
        self.assertEqual(len(bundle["core_scenes"]), 16)
        self.assertEqual(len(bundle["adaptive_questions"]), 6)
        self.assertEqual(len(bundle["animals"]), 18)
        self.assertEqual(set(bundle["results"]), set(bundle["animals"]))
        self.assertEqual(set(bundle["realms"]), {"Taiga", "Desert", "Rainforest"})

    def test_bundle_contains_three_realm_scoring_runtime(self):
        bundle = build_bundle()
        self.assertEqual(bundle["bundle_version"], "0.5")
        self.assertEqual(len(bundle["boundary_questions"]), 16)
        self.assertEqual(len(bundle["scoring"]["animals"]), 18)
        realms = {
            animal["realm"] for animal in bundle["scoring"]["animals"].values()
        }
        self.assertEqual(realms, {"Taiga", "Desert", "Rainforest"})
        self.assertEqual(
            bundle["scoring"]["classification_policy"],
            "soft_realm_then_conditional_animal",
        )
        self.assertEqual(
            bundle["scoring"]["realm_pooling"],
            "mean_animal_likelihood",
        )
        self.assertEqual(bundle["scoring"]["max_adaptive_questions"], 2)

    def test_generated_bundle_is_current(self):
        self.assertTrue(DEFAULT_OUTPUT.exists())
        self.assertEqual(DEFAULT_OUTPUT.read_text(encoding="utf-8"), render_bundle())


if __name__ == "__main__":
    unittest.main()
