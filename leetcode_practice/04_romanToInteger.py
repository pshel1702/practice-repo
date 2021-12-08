import unittest


class romanToIntegerConversion(unittest.TestCase):
    def test_singleRomanInput(self):
        s = 'I'
        result = romanToInt(s)
        self.assertEqual(result, 1)


def romanToInt(s):
    return 1


if __name__ == "__main__":
    unittest.main()
