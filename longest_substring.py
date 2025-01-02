import unittest


def length_of_longest_substring(s: str) -> int:
    max_length = 0
    left = 0
    seen = set()
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        max_length = max(max_length, right - left + 1)
        seen.add(s[right])
    return max_length


class TestLongestSubstring(unittest.TestCase):
    def test1(self):
        s = 'abcabcbb'
        self.assertEqual(3, length_of_longest_substring(s))

    def test2(self):
        s = 'bbbbb'
        self.assertEqual(1, length_of_longest_substring(s))

    def test3(self):
        s = 'pwwkew'
        self.assertEqual(3, length_of_longest_substring(s))

