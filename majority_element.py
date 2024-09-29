import unittest
from collections import Counter


def majority_element(nums: list[int]) -> int:
    m = Counter(nums)
    n = len(nums)
    for num in m:
        if m[num] > n / 2:
            return num


class TestMajorityElement(unittest.TestCase):
    def test_majority1(self):
        nums = [3, 2, 3]
        self.assertEqual(3, majority_element(nums))

    def test_majority2(self):
        nums = [2, 2, 1, 1, 1, 2, 2]
        self.assertEqual(2, majority_element(nums))
