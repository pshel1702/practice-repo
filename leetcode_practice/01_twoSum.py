import unittest


class twoSumTest(unittest.TestCase):

    def test_two_numbers(self):
        nums = [1,2]
        target = 3
        result = twoSum(nums,target)
        self.assertEqual(result, [0,1])
    
    def test_four_numbers(self):
        nums = [2,7,11,15]
        target = 9
        result = twoSum(nums,target)
        self.assertEqual(result,[0,1])   

    def test_three_numbers(self):
        nums = [3,2,4]
        target = 6
        result = twoSum(nums,target)
        self.assertEqual(result,[1,2])  


def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
    

if __name__=="__main__":
    unittest.main()
