import unittest

class palindromeNumberTest(unittest.TestCase):

    def test_singleDigit(self):
        num = 1
        result = isPalindrome(num)
        self.assertTrue(result)

    def test_twoDifferentDigits(self):
        num = 23
        result = isPalindrome(num)
        self.assertFalse(result)
    
    def test_threePalindromeDigits(self):
        num = 121
        result = isPalindrome(num)
        self.assertTrue(result)
    
    def test_fivePalindromeDigits(self):
        num = 12321
        result = isPalindrome(num)
        self.assertTrue(result)

    def test_fiveNonPalindromeDigits(self):
        num = 12231
        result = isPalindrome(num)
        self.assertFalse(result)

    def test_negativeNonPalindrome(self):
        num = -131
        result = isPalindrome(num)
        self.assertFalse(result)


def isPalindrome(num):
    num_as_str = str(num)
    #return num_as_str[0] == num_as_str[-1]
    return num_as_str == num_as_str[::-1]


#execute our module as a script
if __name__== "__main__":
    unittest.main()


#Structure of unit tests:
#Arrange [set up test case]
#Act [invoke the test -> what is the action i'm doing]
#Assert 