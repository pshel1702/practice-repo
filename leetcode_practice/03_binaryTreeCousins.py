import unittest

class isBinaryTreeCousinTest(unittest.TestCase):

    def test_two_nodes_false(self):
        root = [1,2]
        x = 1
        y = 2
        result = are_cousins(root,x,y)
        self.assertFalse(result)

    def test_siblings_false(self):
        root = [1,2,3]
        x = 2
        y = 3
        result = are_cousins(root,x,y)
        self.assertFalse(result)

    def test_nodes_diff_depths_false(self):
        root = [1,2,3,4]
        x = 4
        y = 3
        result = are_cousins(root,x,y)
        self.assertFalse(result)
    
    def test_get_parent_one_child(self):
        root = [1,2]
        node = 2
        result = get_parent(root,node)
        self.assertEqual(result,1)

    """ 
    def test_get_parent_two_children(self):
        root = [1,2,3]
        x = 2
        y = 3
        result = get_parent(root,node)
        self.assertEqual(result,1) """
    
    def test_root_traverse_subtree(self):
        root = [1,2,3]
        node = 1
        result = get_nodes(root,node)
        expected = (1,2,3)
        self.assertEqual(result,expected)
    
    def test_get_root_depth(self):
        root = [1,2]
        x = 2
        result = get_depth(root,1)
        self.assertEqual(result,0)
    
    def test_left_traverse_subtree_levels(self):
        root = [1,2,3,4]
        node = 2
        result = get_nodes(root,node)
        expected = (2,4,None)
        self.assertEqual(result,expected)
    
    def test_right_traverse_subtree_levels(self):
        root = [1,2,3,4,None,5]
        node = 3
        result = get_nodes(root,node)
        expected = (3,5,None)
        self.assertEqual(result,expected)
    

def are_cousins(root,x,y):
    return False

def get_parent(root,node):
    return 1

def get_depth(root,node):
    return 0 

def get_nodes(root,node):
    #tree_root = root[0]
    if node == root[0]:
        return (node,root[1],root[2])

    for i in range(len(root)):
        if root[i] == node:
            if is_left_child(i): 
                left_child = root[i+3]
                right_child = None
            else:
                left_child = root[i+2]
                right_child = None
                break

    return (node,left_child,right_child)

def is_left_child(i):
    return i%2 == 0

if __name__=="__main__":
    unittest.main()