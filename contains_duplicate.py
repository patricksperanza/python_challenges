import unittest


def contains_duplicate(nums):
    uniques = set(nums)
    return len(nums) != len(uniques)


class TestContainsDuplicate(unittest.TestCase):
    def test_contains_duplicate1(self):
        nums = [1, 2, 3, 1]
        self.assertTrue(contains_duplicate(nums))

    def test_contains_duplicate2(self):
        nums = [1, 2, 3, 4]
        self.assertFalse(contains_duplicate(nums))

    def test_contains_duplicate3(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        self.assertTrue(contains_duplicate(nums))

