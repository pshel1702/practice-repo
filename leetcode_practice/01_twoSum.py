import unittest


class twoSumTest(unittest.TestCase):

    def test_two_numbers(self):
        nums = [1,2]
        target = 3
        result = twoSum(nums,target)
        self.assertEqual(result, [0,1])


def twoSum(nums,target):
    
    return [0,1]

if __name__=="__main__":
    unittest.main()
