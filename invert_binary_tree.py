import unittest
from typing import Optional


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_binary_tree(root: Optional[Node]) -> Optional[Node]:
    if not root:
        return
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)
    root.left, root.right = root.right, root.left
    return root


class TestInvertBinaryTree(unittest.TestCase):
    def test1(self):
        root = Node(4, Node(2, Node(1), Node(3)), Node(7, Node(6), Node(9)))
        invert_binary_tree(root)
        self.assertEqual(4, root.val)
        self.assertEqual(7, root.left.val)
        self.assertEqual(2, root.right.val)
        self.assertEqual(9, root.left.left.val)
        self.assertEqual(6, root.left.right.val)
        self.assertEqual(3, root.right.left.val)
        self.assertEqual(1, root.right.right.val)

    def test2(self):
        root = Node(2, Node(1), Node(3))
        invert_binary_tree(root)
        self.assertEqual(2, root.val)
        self.assertEqual(3, root.left.val)
        self.assertEqual(1, root.right.val)
