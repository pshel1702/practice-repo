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
    for index, symbol in enumerate(s):
        if index+1 < len(s) and roman_to_integer_dict[symbol] < roman_to_integer_dict[s[index+1]]:
            temp = roman_to_integer_dict[s[index+1]
                                         ] - roman_to_integer_dict[symbol]
            val += temp
            break
        elif index < len(s):
            temp = roman_to_integer_dict[symbol]
        val += temp

    return val


if __name__ == "__main__":
    unittest.main()
