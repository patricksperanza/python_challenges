import unittest


def is_subsequence(s, t):
    if s == "":
        return True
    i = 0
    n = len(s)
    for j in range(len(t)):
        if t[j] == s[i]:
            i += 1
            if i >= n:
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
