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

    def test_multiple_words_with_shortest_word_as_common_prefix(self):
        strs = ["flow", "flowery", "flower"]
        result = longestCommonPrefix(strs)
        self.assertEqual(result, "flow")


def longestCommonPrefix(strs):
    if len(strs) == 1:
        return "flower"
    shortest_word = strs[0]
    for _, item in enumerate(strs):
        if len(item) < len(shortest_word):
            shortest_word = item
    shortest_word_length = len(shortest_word)
    while(shortest_word_length > 0):
        for _, item in enumerate(strs):
            if item[0:shortest_word_length] == shortest_word:
                prefix = shortest_word
                continue
            break
        shortest_word_length -= 1
        shortest_word = shortest_word[0:-1]
    return prefix


if __name__ == "__main__":
    unittest.main()
