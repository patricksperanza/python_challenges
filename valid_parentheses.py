import unittest


def is_valid(s):
    hashmap = {')': '(', '}': '{', ']': '['}
    stk = []
    for c in s:
        if c not in hashmap:
            stk.append(c)
        else:
            if not stk:
                return False
            else:
                popped = stk.pop()
                if popped != hashmap[c]:
                    return False
    return not stk


class TestIsValid(unittest.TestCase):
    def test_is_valid1(self):
        s = "()"
        self.assertTrue(is_valid(s))

    def test_is_valid2(self):
        s = "()[]{}"
        self.assertTrue(is_valid(s))

    def test_is_valid3(self):
        s = "(]"
        self.assertFalse(is_valid(s))

    def test_is_valid4(self):
        s = "([])"
        self.assertTrue(is_valid(s))



