import unittest

from scripts.export_web_bundle import DEFAULT_OUTPUT, build_bundle, render_bundle


class WebBundleV01Tests(unittest.TestCase):
    def test_bundle_contains_complete_taiga_runtime(self):
        bundle = build_bundle()
        self.assertEqual(len(bundle["core_scenes"]), 16)
        self.assertEqual(len(bundle["adaptive_questions"]), 6)
        self.assertEqual(len(bundle["animals"]), 6)
        self.assertEqual(set(bundle["results"]), set(bundle["animals"]))

    def test_generated_bundle_is_current(self):
        self.assertTrue(DEFAULT_OUTPUT.exists())
        self.assertEqual(DEFAULT_OUTPUT.read_text(encoding="utf-8"), render_bundle())


if __name__ == "__main__":
    unittest.main()
