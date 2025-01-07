import unittest


def is_subsequence(s, t):
    sp = tp = 0
    while sp < len(s) and tp < len(t):
        if s[sp] == t[tp]:
            sp += 1
        tp += 1
    return sp == len(s)


class TestIsSubsequence(unittest.TestCase):
    def test_1(self):
        s = 'abc'
        t = 'ahbgdc'
        self.assertTrue(is_subsequence(s, t))

    def test_2(self):
        s = 'axc'
        t = 'ahbgdc'
        self.assertFalse(is_subsequence(s, t))
