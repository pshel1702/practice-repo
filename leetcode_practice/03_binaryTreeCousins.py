import unittest

class BinaryTreeCousinsAcceptanceTests(unittest.TestCase):
    
    def test_are_cousins_false(self):
        root = [1,2,3,4]
        x = 4
        y = 3
        result = are_cousins(root,x,y)
        self.assertFalse(result)

    def test_are_cousins_true(self):
        root = [1,2,3,None,4,None,5]
        x = 5
        y = 4
        result = are_cousins(root,x,y)
        self.assertTrue(result)
    
    def test_are_cousins_left_node_with_two_children_false(self):
        root = [1,2,3,None,4]
        x = 2
        y = 3
        result = are_cousins(root,x,y)
        self.assertFalse(result)
    
    def test_are_cousins_third_level_true(self):
        root = [1,2,3,4,5,6,7,8,9,10,11,12]
        x = 8
        y = 12
        result = are_cousins(root,x,y)
        self.assertTrue(result)

    def test_are_cousins_third_level_siblings_false(self):
        root = [1,2,3,4,5,6,7,8,9,10,11,12]
        x = 10
        y = 11
        result = are_cousins(root,x,y)
        self.assertFalse(result)
    
    def test_are_cousins_parent_child_false(self):
        root = [1,2,3,4,5,6,7,8,9,10,11,12]
        x = 5
        y = 11
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
    
    def test_get_parent_child_at_second_level(self):
        root = [1,2,3,4]
        node = 4
        result = get_parent(root,node)
        self.assertEqual(result,2)

    def test_get_depth_root(self):
        root = [1]
        node = 1
        result = get_depth(root,node)
        self.assertEqual(result,0)
    
    def test_get_depth_root_one_child(self):
        root = [1,2]
        node = 2
        result = get_depth(root,node)
        self.assertEqual(result,1)
    
    def test_get_depth_root_with_two_children(self):
        root = [1,2,3]
        node = 3
        result = get_depth(root,node)
        self.assertEqual(result,1)
    
    def test_get_depth_node_at_second_level(self):
        root = [1,2,3,4]
        node = 4
        result = get_depth(root,node)
        self.assertEqual(result,2)
    
    def test_get_depth_leftmost_node_at_third_level(self):
        level_0 = [1]
        level_1 = [2,3]
        level_2 = [4,5,6,7]
        level_3 = [8]
        root = [*level_0,*level_1,*level_2,*level_3]
        node = 8
        result = get_depth(root,node)
        self.assertEqual(result,3)
    
    def test_get_depth_rightmost_node_at_third_level(self):
        level_0 = [1]
        level_1 = [2,3]
        level_2 = [4,5,6,7]
        level_3 = [8,9,10,11,12,13,14,15]
        root = [*level_0,*level_1,*level_2,*level_3]
        node = 15
        result = get_depth(root,node)
        self.assertEqual(result,3)

    def test_get_depth_middle_node_at_third_level(self):
        level_0 = [1]
        level_1 = [2,3]
        level_2 = [4,5,6,7]
        level_3 = [8,9,10,11,12,13,14,15]
        root = [*level_0,*level_1,*level_2,*level_3]
        node = 12
        result = get_depth(root,node)
        self.assertEqual(result,3)
    
    def test_get_depth_leftmost_node_at_fourth_level(self):
        level_0 = [1]
        level_1 = [2,3]
        level_2 = [4,5,6,7]
        level_3 = [8,9,10,11,12,13,14,15]
        level_4 = [16]
        root = [*level_0,*level_1,*level_2,*level_3,*level_4]
        node = 16
        result = get_depth(root,node)
        self.assertEqual(result,4)
    
    def test_get_depth_rightmost_node_at_fourth_level(self):
        level_0 = [1]
        level_1 = [2,3]
        level_2 = [4,5,6,7]
        level_3 = [8,9,10,11,12,13,14,15]
        level_4 = [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
        root = [*level_0,*level_1,*level_2,*level_3,*level_4]
        node = 31
        result = get_depth(root,node)
        self.assertEqual(result,4)

def get_depth(root,node):
    node_index = root.index(node)
    if node_index in (1,2):
        return 1
    if node_index in range(3,7):
        return 2
    if node_index in range(7,15):
        return 3
    if node_index in range(15,31):
        return 4
    
    return 0

def get_parent(root,node):
    #Pseudocode
    #iterate over root to find node
    #if index of node is even, parent == root[i-3], else parent == root[i-2]
    node_index = root.index(node)
    #add function to check index
    if(node_index==1) or (node_index==2):
        return root[0]

    if(node_index%2 == 0):
        return root[node_index-3]
    return root[node_index-2]

    
def are_cousins(root,x,y):
    ##Pseudocode
    #Find parent and depth of x in root
    #Repeat above step for y in root
    #Return True if parent_x != parent_y and depth_x == depth_y
    #Else return False
    
    parent_x = get_parent(root,x)
    parent_y = get_parent(root,y)
    depth_x = get_depth(root,x)
    depth_y = get_depth(root,y)
    #print(f'Parent,depth of {x} is {parent_x},{depth_x} and that of {y} and {parent_y},{depth_y}')
    if(parent_x!=parent_y) and depth_x == depth_y:
        return True
    return False



if __name__ == "__main__":
    unittest.main()