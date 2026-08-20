import unittest

from scripts.simulate_questions import load_bank
from scripts.taiga_story import load_story, merge_story, story_errors


class TaigaStoryOverlayV01Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bank = load_bank()
        cls.story = load_story()
        cls.scenes = merge_story(cls.story, cls.bank)

    def test_story_schema_and_coverage(self):
        self.assertEqual(story_errors(self.story, self.bank), [])

    def test_measurement_evidence_is_unchanged(self):
        original = {
            question["id"]: [option["evidence"] for option in question["options"]]
            for question in self.bank["questions"]
        }
        merged = {
            scene["id"]: [option["evidence"] for option in scene["options"]]
            for scene in self.scenes
        }
        self.assertEqual(merged, original)

    def test_story_order_matches_spine(self):
        self.assertEqual(
            [scene["id"] for scene in self.scenes],
            [
                "Q02", "Q03", "Q01", "Q04",
                "Q07", "Q06", "Q05", "Q08", "Q09", "Q10",
                "Q11", "Q12", "Q13", "Q14", "Q15", "Q16",
            ],
        )

    def test_every_option_has_continuity_tags(self):
        for scene in self.scenes:
            for option in scene["options"]:
                self.assertTrue(option["consequence_tags"])


if __name__ == "__main__":
    unittest.main()
