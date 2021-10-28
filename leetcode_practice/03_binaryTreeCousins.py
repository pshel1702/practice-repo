import unittest

class BinaryTreeCousinsAcceptanceTests(unittest.TestCase):
    
    def test_are_cousins_false(self):
        root = [1,2,3,4]
        x = 4
        y = 3
        result = are_cousins(root,x,y)
        self.assertFalse(result)

def are_cousins(root,x,y):
    raise


if __name__ == "__main__":
    unittest.main()