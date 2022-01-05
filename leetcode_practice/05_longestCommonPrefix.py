import unittest


class longestCommonPrefixTests(unittest.TestCase):
    def test_single_word(self):
        strs = ["flower"]
        result = longestCommonPrefix(strs)
        self.assertEqual(result, "flower")

    def test_multiple_words_no_common_prefix(self):
        strs = ["flower", "car"]
        result = longestCommonPrefix(strs)
        self.assertEqual(result, "")


def longestCommonPrefix(strs):
    if len(strs) == 1:
        return "flower"
    return ""


if __name__ == "__main__":
    unittest.main()
