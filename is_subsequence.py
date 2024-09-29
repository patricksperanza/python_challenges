import unittest


def is_subsequence(s: str, t: str) -> bool:
    n1, n2 = len(s), len(t)
    if n1 > n2: return False
    if s == '': return True
    i = 0
    for j in range(n2):
        if s[i] == t[j]:
            i += 1
            if i == n1:
                return True
    return False



class TestIsSubsequence(unittest.TestCase):
    def test_1(self):
        s = 'abc'
        t = 'ahbgdc'
        self.assertTrue(is_subsequence(s, t))

    def test_2(self):
        s = 'axc'
        t = 'ahbgdc'
        self.assertFalse(is_subsequence(s, t))

