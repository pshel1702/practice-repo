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
    temp = 0
    skip_iteration = False
    for index, symbol in enumerate(s):
        if skip_iteration:
            skip_iteration = False
            continue
        if index+1 < len(s) and roman_to_integer_dict[symbol] < roman_to_integer_dict[s[index+1]]:
            temp = roman_to_integer_dict[s[index+1]
                                         ] - roman_to_integer_dict[symbol]
            val += temp
            skip_iteration = True
        elif index < len(s):
            temp = roman_to_integer_dict[symbol]
            skip_iteration = False
            val += temp

    return val


if __name__ == "__main__":
    unittest.main()
