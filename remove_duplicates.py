import unittest
from typing import Optional


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head: Optional[Node]) -> Optional[Node]:
    cur = head
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head


class TestDeleteDuplicates(unittest.TestCase):
    def test1(self):
        node1 = Node(1)
        node2 = Node(1)
        node3 = Node(2)
        node1.next = node2
        node2.next = node3
        head = delete_duplicates(node1)
        result = []
        curr = head
        while curr:
            result.append(curr.val)
            curr = curr.next
        self.assertEqual([1, 2], result)

    def test2(self):
        node1 = Node(1)
        node2 = Node(1)
        node3 = Node(2)
        node4 = Node(3)
        node5 = Node(3)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        head = delete_duplicates(node1)
        result = []
        curr = head
        while curr:
            result.append(curr.val)
            curr = curr.next
        self.assertEqual([1, 2, 3], result)
