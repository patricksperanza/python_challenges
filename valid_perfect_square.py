import unittest


def is_perfect_square(num: int) -> bool:
    left = 1
    right = num
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == num:
            return True
        elif mid * mid < num:
            left = mid + 1
        else:
            right = mid - 1
    return False


class Test(unittest.TestCase):
    def test_is_perfect_square(self):
        self.assertTrue(is_perfect_square(9))
        self.assertTrue(is_perfect_square(16))
        self.assertTrue(is_perfect_square(25))
        self.assertTrue(is_perfect_square(36))
        self.assertTrue(is_perfect_square(100))
        self.assertFalse(is_perfect_square(10))
        self.assertFalse(is_perfect_square(17))
        self.assertFalse(is_perfect_square(37))
        self.assertFalse(is_perfect_square(101))
