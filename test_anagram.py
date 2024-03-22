import unittest
import anagram


class TestAnagram(unittest.TestCase):
    def test_get_anagram(self):
        anagrams = anagram.Anagrams()

        test_cases = [
            ("plates", {"palest", "pastel", "petals", "plates", "staple"}),
            ("eat", {"ate", "eat", "tea"}),
            ("x", None),
            (
                "   ",
                "Invalid Input: Please provide a word to check",
            ),
            (
                "abc123",
                "Invalid Input: Entered word 'abc123' is not a correct word. Please enter a correct word!",
            ),
            (
                "12345abc",
                "Invalid Input: Entered word '12345abc' is not a correct word. Please enter a correct word!",
            ),
            (
                "file/path",
                "Invalid Input: Entered word 'file/path' is not a correct word. Please enter a correct word!",
            ),
            (
                "12345",
                "Invalid Input: Entered word '12345' is not a correct word. Please enter a correct word!",
            ),
            ("Eat", {"ate", "eat", "tea"}),
            ("EAT", {"ate", "eat", "tea"}),
            ("EAT ", {"ate", "eat", "tea"}),
            (" EAT", {"ate", "eat", "tea"}),
            (" EAT ", {"ate", "eat", "tea"}),
            ("EAT            ", {"ate", "eat", "tea"}),
            ("              EAT", {"ate", "eat", "tea"}),
            ("        EAT            ", {"ate", "eat", "tea"}),
            ("abcdefghijklmnopqrstuvwxyz", None),
        ]

        for input, expected_result in test_cases:
            result = anagrams.get_anagrams(input)
            if isinstance(result,list):
                self.assertSetEqual(set(result), expected_result)
            else:
                self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
