import unittest
from typing import Optional


class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[Node]) -> Optional[Node]:
    curr = head
    prev = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


class TestReverseList(unittest.TestCase):
    def test1(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        head = reverse_list(node1)
        result = []
        curr = head
        while curr:
            result.append(curr.val)
            curr = curr.next
        self.assertEqual([5, 4, 3, 2, 1], result)

    def test2(self):
        node1 = Node(1)
        node2 = Node(2)
        node1.next = node2
        head = reverse_list(node1)
        result = []
        curr = head
        while curr:
            result.append(curr.val)
            curr = curr.next
        self.assertEqual([2, 1], result)
