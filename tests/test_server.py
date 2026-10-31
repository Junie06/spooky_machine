import unittest
from unittest.mock import patch

import server


class StoryGeneratorTests(unittest.TestCase):
    def test_empty_seed_uses_default_haunting_idea(self):
        self.assertIn("lonely house", server.build_prompt("  "))

    def test_story_idea_is_limited_to_500_characters(self):
        self.assertEqual(len(server.build_prompt("a" * 700)), 500)

    def test_story_response_contains_only_the_finished_story(self):
        result = {"response": "<think>private planning</think>\nThe door opened."}
        self.assertEqual(server.clean_story_response(result), "The door opened.")

    def test_rejects_truncated_thinking_instead_of_showing_it(self):
        with self.assertRaisesRegex(server.ModelError, "did not finish"):
            server.clean_story_response({"response": "<think>private planning"})

    def test_rejects_non_local_ollama_endpoint(self):
        with patch.dict("os.environ", {"OLLAMA_URL": "https://example.com/api/generate"}):
            with self.assertRaisesRegex(server.ModelError, "running locally"):
                server.ollama_endpoint()


if __name__ == "__main__":
    unittest.main()
