import unittest


def is_palindrome(s: str) -> bool:
    s = [c.lower() for c in s if c.isalnum()]
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
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
