import unittest
from unittest.case import skip

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

    def test_subtraction_scenario(self):
        s = "IV"
        result = romanToInt(s)
        self.assertEqual(result, 4)

    def test_subtraction_scenario_four_symbols(self):
        s = "XXIV"
        result = romanToInt(s)
        self.assertEqual(result, 24)

    def test_subtraction_multiple_symbols(self):
        s = "LVIII"
        result = romanToInt(s)
        self.assertEqual(result, 58)

    def test_subtraction_multiple_symbols(self):
        s = "MCMXCIV"
        result = romanToInt(s)
        self.assertEqual(result, 1994)


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
    for index, symbol in enumerate(s):
        curr_symbol_val = roman_to_integer_dict[symbol]
        if to_subtract(index, s, curr_symbol_val):
            val -= curr_symbol_val
        else:
            val += curr_symbol_val

    return val


def to_subtract(index, s, curr_symbol_val):
    return index+1 < len(s) and curr_symbol_val < roman_to_integer_dict[s[index+1]]


if __name__ == "__main__":
    unittest.main()
