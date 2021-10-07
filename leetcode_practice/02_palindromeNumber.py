import unittest

class palindromeNumberTest(unittest.TestCase):

    def test_singleDigit(self):
        num = 1
        result = isPalindrome(num)
        self.assertEqual(result,True)


def isPalindrome(num):
    return True


#execute our module as a script
if __name__== "__main__":
    unittest.main()


#Structure of unit tests:
#Arrange [set up test case]
#Act [invoke the test -> what is the action i'm doing]
#Assert 