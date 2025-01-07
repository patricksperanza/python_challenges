import unittest
from collections import deque, defaultdict


def valid_path(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    if source == destination:
        return True
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    stk = [source]
    seen = set()
    seen.add(source)
    while stk:
        node = stk.pop()
        if node == destination:
            return True
        else:
            for neighbor in graph[node]:
                if neighbor not in seen:
                    stk.append(neighbor)
                    seen.add(neighbor)
    return False


class TestValidPath(unittest.TestCase):
    def test1(self):
        n = 3
        edges = [[0, 1], [1, 2], [2, 0]]
        source = 0
        destination = 0
        self.assertTrue(valid_path(n, edges, source, destination))

    def test2(self):
        n = 6
        edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
        source = 0
        destination = 5
        self.assertFalse(valid_path(n, edges, source, destination))
