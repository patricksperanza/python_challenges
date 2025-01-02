import unittest


def merge_strings(word1, word2):
    res = []
    n = min(len(word1), len(word2))
    i = 0
    while i < n:
        res.append(word1[i] + word2[i])
        i += 1
    if len(word1) > n:
        res.append(word1[i:])
    elif len(word2) > n:
        res.append(word2[i:])
    return "".join(res)


class TestMerge(unittest.TestCase):
    def test_merge1(self):
        word1 = "abc"
        word2 = "pqr"
        self.assertEqual("apbqcr", merge_strings(word1, word2))

    def test_merge2(self):
        word1 = "ab"
        word2 = "pqrs"
        self.assertEqual("apbqrs", merge_strings(word1, word2))
