from collections import deque
import unittest


class Node:
    def __init__(self, val: int, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


def breadth_first_traversal(root: Node) -> list[list[int]]:
    if not root:
        return []

    q = deque([root])
    result = []
    while q:
        n = len(q)
        level = []
        for _ in range(n):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)
    return result


class TestBreadthFirstTraversal(unittest.TestCase):
    def test1(self):
        root = Node(3)
        root.left = Node(9)
        root.right = Node(20)
        root.right.left = Node(15)
        root.right.right = Node(17)
        expected = [[3], [9, 20], [15, 17]]
        actual_result = breadth_first_traversal(root)
        self.assertEqual(expected, actual_result)
