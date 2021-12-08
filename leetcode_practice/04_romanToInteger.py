import unittest

from ddt import ddt, data, unpack


@ddt
class romanToIntegerConversion(unittest.TestCase):
    @data(('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000))
    @unpack
    def test_standard_roman_symbols(self, s, expected):
        result = romanToInt(s)
        self.assertEqual(result, expected)

    def test_repeated_roman_symbols(self):
        s = "III"
        result = romanToInt(s)
        self.assertEqual(result, 3)


roman_to_integer_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def romanToInt(s):
    val = 0
    for symbol in s:
        val += roman_to_integer_dict[symbol]
    return val


if __name__ == "__main__":
    unittest.main()
