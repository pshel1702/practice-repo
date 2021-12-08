import unittest

from ddt import ddt, data, unpack


@ddt
class romanToIntegerConversion(unittest.TestCase):
    @data(('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000))
    @unpack
    def test_standard_roman_symbols(self, s, expected):
        result = romanToInt(s)
        self.assertEqual(result, expected)


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
    return roman_to_integer_dict[s]


if __name__ == "__main__":
    unittest.main()
