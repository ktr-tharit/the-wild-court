import unittest

from scripts.session_runner import TaigaSession, run_profile


class TaigaSessionRunnerV01Tests(unittest.TestCase):
    def test_session_starts_at_first_story_scene(self):
        session = TaigaSession()
        self.assertEqual(session.phase, "Arrival")
        self.assertEqual(session.current_question()["id"], "Q02")

    def test_rejects_wrong_question_and_invalid_option(self):
        session = TaigaSession()
        with self.assertRaises(ValueError):
            session.submit("A", question_id="Q01")
        with self.assertRaises(ValueError):
            session.submit("E")

    def test_all_six_profile_journeys_finish(self):
        for animal in TaigaSession().model["animals"]:
            with self.subTest(animal=animal):
                session = run_profile(animal)
                result = session.public_result()
                self.assertTrue(session.is_complete)
                self.assertIn(result["primary_animal"], session.model["animals"])
                self.assertGreaterEqual(result["questions_answered"], 16)
                self.assertLessEqual(result["questions_answered"], 18)

    def test_public_result_hides_measurement_details(self):
        result = run_profile("Grey Wolf").public_result()
        self.assertNotIn("internal", result)
        self.assertNotIn("player_vector", result)
        self.assertNotIn("ranking", result)

    def test_audit_result_contains_complete_response_log(self):
        result = run_profile("Reindeer").audit_result()
        self.assertEqual(
            len(result["internal"]["responses"]), result["questions_answered"]
        )
        self.assertEqual(len(result["internal"]["player_vector"]), 8)

    def test_story_tags_create_callbacks(self):
        result = run_profile("Wolverine").public_result()
        self.assertTrue(result["continuity_tags"])
        self.assertTrue(result["callbacks"])


if __name__ == "__main__":
    unittest.main()
