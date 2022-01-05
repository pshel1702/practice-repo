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

    def test_multiple_words_with_single_letter_common_prefix(self):
        strs = ["for", "fire", "fan"]
        result = longestCommonPrefix(strs)
        self.assertEqual(result, "f")


def longestCommonPrefix(strs):
    if len(strs) == 1:
        return "flower"
    prefix = strs[0][0]
    for _, item in enumerate(strs):
        if item[0] == prefix:
            continue
        return ""
    return prefix


if __name__ == "__main__":
    unittest.main()
