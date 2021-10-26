import unittest

class isBinaryTreeCousinTest(unittest.TestCase):

    def test_two_nodes_false(self):
        root = [1,2]
        x = 1
        y = 2
        result = are_cousins(root,x,y)
        self.assertFalse(result)
    
    def test_nodes_true(self):
        root = [1,2,3,None,4,None,5]
        x = 4
        y = 5
        result = are_cousins(root,x,y)
        self.assertTrue(result)

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
    
    def test_get_parent_child_at_first_level(self):
        root = [1,2]
        node = 2
        result = get_parent(root,node)
        self.assertEqual(result,1)
    
    def test_get_parent_child_at_second_level(self):
        root = [1,2,None,3]
        node = 3
        result = get_parent(root,node)
        self.assertEqual(result,2)

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
    
    def test_get_nodes_left_node_with_left_child_only(self):
        root = [1,2,3,4]
        node = 2
        result = get_nodes(root,node)
        expected = (2,4,None)
        self.assertEqual(result,expected)
    
    def test_get_nodes_right_node_with_left_child_only(self):
        root = [1,2,3,4,None,5]
        node = 3
        result = get_nodes(root,node)
        expected = (3,5,None)
        self.assertEqual(result,expected)
    
    def test_get_nodes_right_child_with_two_children(self):
        root = [1,2,3,4,None,5,6]
        node = 3
        result = get_nodes(root,node)
        expected = (3,5,6)
        self.assertEqual(result,expected)
    
    def test_get_nodes_left_child_with_two_children(self):
        root = [1,2,3,4,5,6]
        node = 2
        result = get_nodes(root,node)
        expected = (2,4,5)
        self.assertEqual(result,expected)
  

def are_cousins(root,x,y):
    parent_x = get_parent(root,x)
    parent_y = get_parent(root,y)
    return parent_x != parent_y
        
def get_parent(root,node):
    for i in root:
        result = get_nodes(root, i)
        if result[1]== node or result[2] == node:
            parent = i
            break
    return parent

def get_nodes(root,node):
    #tree_root = root[0]
    if node == root[0]:
        return (node,root[1],root[2])

    right_child = None
    root_length = len(root)
    for i,value in enumerate(root):
        if value == node:
            if is_right_child(i): 
                left_child = root[i+3]
                if i+4<root_length:
                    right_child = root[i+4]
                break
            else:
                left_child = root[i+2]
                if i+3<root_length:
                    right_child = root[i+3]
                break

    return (node,left_child,right_child)


def is_right_child(i):
    return i%2 == 0


if __name__=="__main__":
    unittest.main()