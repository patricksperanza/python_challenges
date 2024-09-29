import unittest


def is_palindrome(s: str) -> bool:
    l = 0
    r = len(s) - 1
    s = s.lower()
    while l < r:
        if not s[l].isalnum():
            l += 1
            continue
        if not s[r].isalnum():
            r -= 1
            continue
        if not s[l] == s[r]:
            return False
        l += 1
        r -= 1
    return True


class TestValidPalindrome(unittest.TestCase):
    def test_is_valid1(self):
        s = "A man, a plan, a canal: Panama"
        self.assertTrue(is_palindrome(s))

    def test_is_valid2(self):
        s = "race a car"
        self.assertFalse(is_palindrome(s))

    def test_is_valid3(self):
        s = " "
        self.assertTrue(is_palindrome(s))
