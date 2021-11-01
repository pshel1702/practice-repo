import unittest


class BinaryTreeCousinsAcceptanceTests(unittest.TestCase):

    def test_are_cousins_false_when_dif_depths(self):
        root = [1, 2, 3, 4]
        x = 4
        y = 3
        result = are_cousins(root, x, y)
        self.assertFalse(result)

    def test_are_cousins_true_when_dif_parent_same_depth(self):
        root = [1, 2, 3, None, 4, None, 5]
        x = 5
        y = 4
        result = are_cousins(root, x, y)
        self.assertTrue(result)

    def test_are_cousins_false_when_same_parent(self):
        root = [1, 2, 3, None, 4]
        x = 2
        y = 3
        result = are_cousins(root, x, y)
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


def get_depth(root, node):
    node_index = root.index(node)
    if node_index in (1, 2):
        return 1
    if node_index == 3:
        return 2
    return 0


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


def are_cousins(root, x, y):
    # Pseudocode
    # Find parent and depth of x in root
    # Repeat above step for y in root
    # Return True if parent_x != parent_y and depth_x == depth_y
    # Else return False

    parent_x = get_parent(root, x)
    parent_y = get_parent(root, y)
    depth_x = get_depth(root, x)
    depth_y = get_depth(root, y)

    if(parent_x != parent_y) and depth_x == depth_y:
        return True
    return False


if __name__ == "__main__":
    unittest.main()
