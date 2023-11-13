import unittest
from tree import Node
from tree_traversal import in_order_iterative, level_order_iterative


class LibSearchTest(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Node(10)
        self.root.left = Node(5)
        self.root.left.left = Node(3)
        self.root.left.right = Node(7)
        self.root.right = Node(15)
        self.root.right.left = Node(13)
        self.root.right.right = Node(100)

    def test_inorder_iterative(self):
        expected = [3, 5, 7, 10, 13, 15, 100]
        self.assertEqual(expected, in_order_iterative(self.root))

    def test_level_order_iterative(self):
        expected = [10, 5, 15, 3, 7, 13, 100]
        self.assertEqual(expected, level_order_iterative(self.root))


if __name__ == '__main__':
    unittest.main()
