import unittest
from collections import Counter


def can_construct(ransomNote: str, magazine: str) -> bool:
    mag = Counter(magazine)
    for char in ransomNote:
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

"""
Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true"""
