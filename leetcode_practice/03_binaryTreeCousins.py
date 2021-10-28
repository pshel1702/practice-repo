import unittest

class BinaryTreeCousinsAcceptanceTests(unittest.TestCase):
    
    def test_are_cousins_false(self):
        root = [1,2,3,4]
        x = 4
        y = 3
        result = are_cousins(root,x,y)
        self.assertFalse(result)

class BinaryTreeCousinsUnitTests(unittest.TestCase):

    def test_get_parent_root_with_one_child(self): #start basic and build
        root = [1,2]
        node=2
        result = get_parent(root,node)
        self.assertEqual(result,1)
    
    def test_get_parent_root_with_two_children(self): 
        root = [1,2,3]
        node=3
        result = get_parent(root,node)
        self.assertEqual(result,1) 


def get_parent(root,node):
    return 1
    
def are_cousins(root,x,y):
    ##Pseudocode
    #Find parent and depth of x in root
    #Repeat above step for y in root
    #Return True if parent_x != parent_y and depth_x == depth_y
    #Else return False
    raise



if __name__ == "__main__":
    unittest.main()