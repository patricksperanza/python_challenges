import unittest


def merge_strings(word1, word2):
    res = []
    for c1, c2 in zip(word1, word2):
        res.append(c1+c2)
    if len(word1) > len(word2):
        res.append(word1[len(word2):])
    elif len(word2) > len(word1):
        res.append(word2[len(word1):])
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


