import unittest

class isBinaryTreeCousinTest(unittest.TestCase):

    def test_two_nodes_false(self):
        root = [1,2]
        x = 1
        y = 2
        result = are_cousins(root,x,y)
        self.assertFalse(result)

def are_cousins(root,x,y):
    return False


if __name__=="__main__":
    unittest.main()