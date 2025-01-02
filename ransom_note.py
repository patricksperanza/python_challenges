import unittest
from collections import Counter


def can_construct(ransom_note: str, magazine: str) -> bool:
    mag = Counter(magazine)
    for char in ransom_note:
        if mag[char]:
            mag[char] -= 1
        else:
            return False
    return True


class TestRansom(unittest.TestCase):
    def test1(self):
        r = "a"
        m = "b"
        self.assertFalse(can_construct(r, m))

    def test2(self):
        r = "aa"
        m = "ab"
        self.assertFalse(can_construct(r, m))

    def test3(self):
        r = "aa"
        m = "aab"
        self.assertTrue(can_construct(r, m))
