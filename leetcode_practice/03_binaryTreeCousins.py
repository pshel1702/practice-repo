import unittest
from typing import Optional


class BinaryTreeCousinsAcceptanceTests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(BinaryTreeCousinsAcceptanceTests, self).__init__(*args, **kwargs)
        self.sut = Solution()

    def test_isCousins_false(self):
        root = [1, 2, 3, 4]
        x = 4
        y = 3
        result = self.sut.isCousins(root, x, y)
        self.assertFalse(result)

    def test_isCousins_true(self):
        root = [1, 2, 3, None, 4, None, 5]
        x = 5
        y = 4
        result = self.sut.isCousins(root, x, y)
        self.assertTrue(result)

    def test_isCousins_left_node_with_two_children_false(self):
        root = [1, 2, 3, None, 4]
        x = 2
        y = 3
        result = self.sut.isCousins(root, x, y)
        self.assertFalse(result)

    def test_isCousins_third_level_true(self):
        root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        x = 8
        y = 12
        result = self.sut.isCousins(root, x, y)
        self.assertTrue(result)

    def test_isCousins_third_level_siblings_false(self):
        root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        x = 10
        y = 11
        result = self.sut.isCousins(root, x, y)
        self.assertFalse(result)

    def test_isCousins_parent_child_false(self):
        root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        x = 5
        y = 11
        result = self.sut.isCousins(root, x, y)
        self.assertFalse(result)

    def test_isCousins_input_TreeNode(self):
        x = 3
        y = 4
        root = TreeNode(1, TreeNode(2, TreeNode(4, None, None),
                        None), TreeNode(3, None, None))
        result = self.sut.isCousins(root, x, y)
        self.assertFalse(result)


class BinaryTreeCousinsUnitTests(unittest.TestCase):

    def test_get_parent_root_with_one_child(self):  # start basic and build
        root = [1, 2]
        node = 2
        result = get_parent(root, node)
        self.assertEqual(result, 1)

    def test_get_parent_root_with_two_children(self):
        root = [1, 2, 3]
        node = 3
        result = get_parent(root, node)
        self.assertEqual(result, 1)

    def test_get_parent_child_at_second_level(self):
        root = [1, 2, 3, 4]
        node = 4
        result = get_parent(root, node)
        self.assertEqual(result, 2)

    def test_get_depth_root(self):
        root = [1]
        node = 1
        result = get_depth(root, node)
        self.assertEqual(result, 0)

    def test_get_depth_root_one_child(self):
        root = [1, 2]
        node = 2
        result = get_depth(root, node)
        self.assertEqual(result, 1)

    def test_get_depth_root_with_two_children(self):
        root = [1, 2, 3]
        node = 3
        result = get_depth(root, node)
        self.assertEqual(result, 1)

    def test_get_depth_node_at_second_level(self):
        root = [1, 2, 3, 4]
        node = 4
        result = get_depth(root, node)
        self.assertEqual(result, 2)

    def test_get_depth_leftmost_node_at_third_level(self):
        level_0 = [1]
        level_1 = [2, 3]
        level_2 = [4, 5, 6, 7]
        level_3 = [8]
        root = [*level_0, *level_1, *level_2, *level_3]
        node = 8
        result = get_depth(root, node)
        self.assertEqual(result, 3)

    def test_get_depth_rightmost_node_at_third_level(self):
        level_0 = [1]
        level_1 = [2, 3]
        level_2 = [4, 5, 6, 7]
        level_3 = [8, 9, 10, 11, 12, 13, 14, 15]
        root = [*level_0, *level_1, *level_2, *level_3]
        node = 15
        result = get_depth(root, node)
        self.assertEqual(result, 3)

    def test_get_depth_middle_node_at_third_level(self):
        level_0 = [1]
        level_1 = [2, 3]
        level_2 = [4, 5, 6, 7]
        level_3 = [8, 9, 10, 11, 12, 13, 14, 15]
        root = [*level_0, *level_1, *level_2, *level_3]
        node = 12
        result = get_depth(root, node)
        self.assertEqual(result, 3)

    def test_get_depth_leftmost_node_at_fourth_level(self):
        level_0 = [1]
        level_1 = [2, 3]
        level_2 = [4, 5, 6, 7]
        level_3 = [8, 9, 10, 11, 12, 13, 14, 15]
        level_4 = [16]
        root = [*level_0, *level_1, *level_2, *level_3, *level_4]
        node = 16
        result = get_depth(root, node)
        self.assertEqual(result, 4)

    def test_get_depth_rightmost_node_at_fourth_level(self):
        level_0 = [1]
        level_1 = [2, 3]
        level_2 = [4, 5, 6, 7]
        level_3 = [8, 9, 10, 11, 12, 13, 14, 15]
        level_4 = [16, 17, 18, 19, 20, 21, 22,
                   23, 24, 25, 26, 27, 28, 29, 30, 31]
        root = [*level_0, *level_1, *level_2, *level_3, *level_4]
        node = 31
        result = get_depth(root, node)
        self.assertEqual(result, 4)

    def test_convert_tree_to_list(self):
        root = TreeNode(1, None, None)
        result = convert_to_list(root)
        self.assertEqual(result, [1, None, None])

    def test_convert_tree_to_list_two_levels(self):
        root = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
        result = convert_to_list(root)
        self.assertEqual(result, [1, 2, 3, None, None, None, None])

    def test_convert_tree_to_list_three_levels(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4, None, None), None), TreeNode(
            3, TreeNode(6, None, None), TreeNode(7, None, None)))
        result = convert_to_list(root)
        self.assertEqual(result, [1, 2, 3, 4, None, 6,
                         7, None, None, None, None, None, None])


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # Pseudocode
        # Find parent and depth of x in root
        # Repeat above step for y in root
        # Return True if parent_x != parent_y and depth_x == depth_y
        # Else return False
        if type(root) == TreeNode:
            list_root = convert_to_list(root)
        else:
            list_root = root
        parent_x = get_parent(list_root, x)
        parent_y = get_parent(list_root, y)
        depth_x = get_depth(list_root, x)
        depth_y = get_depth(list_root, y)
        #print(f'Parent,depth of {x} is {parent_x},{depth_x} and that of {y} and {parent_y},{depth_y}')
        if(parent_x != parent_y) and depth_x == depth_y:
            return True
        return False


def get_depth(root, node):
    # binary tree, every level can have 2^level nodes
    # First level = index is 0
    # Second index starts at 1, ends at 2
    # Left index from level 1: (2^level)-1
    # Right index from level 1: (2^(level+1)-1)

    node_index = root.index(node)

    if node_index in range(1, 3):  # (2^1)-1 = 1, 2^(2)-1 = 3
        return 1
    if node_index in range(3, 7):  # (2^2)-1 = 3, 2^(3)-1 = 7
        return 2
    if node_index in range(7, 15):  # (2^3)-1 = 7, 2^(4)-1 = 15
        return 3
    if node_index in range(15, 31):  # (2^4)-1 = 15, 2^(5)-1 = 31
        return 4
    if node_index in range(31, 63):  # (2^4)-1 = 15, 2^(5)-1 = 31
        return 5
    if node_index in range(63, 100):  # (2^5)-1 = 15, 2^(7)-127 = 31
        return 6

    return 0


def convert_to_list(root: TreeNode):
    result = []
    curr = root
    children = []
    # get curr, take left and right children. then get the children at the next level
    #result = 1,2,3,4,None
    #children  = 7,None,None
    #curr = 6

    result.append(curr.val)
    # method for this repetitive section:
    # explore recursion
    if curr.left:
        children.append(curr.left)
    else:
        children.append(None)
    if curr.right:
        children.append(curr.right)
    else:
        children.append(None)

    while len(children) > 0:
        curr = children[0]
        children[:] = children[1:]
        if not curr:
            result.append(None)
            continue
        result.append(curr.val)
        if curr.left:
            children.append(curr.left)
        else:
            children.append(None)
        if curr.right:
            children.append(curr.right)
        else:
            children.append(None)

    return result


def get_parent(root, node):
    # Pseudocode
    # iterate over root to find node
    # if index of node is even, parent == root[i-3], else parent == root[i-2]
    node_index = root.index(node)
    # add function to check index
    if(node_index == 1) or (node_index == 2):
        return root[0]

    if(node_index % 2 == 0):
        return root[node_index-3]
    return root[node_index-2]


if __name__ == "__main__":
    unittest.main()
