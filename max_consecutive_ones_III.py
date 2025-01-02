import unittest


def longest_ones(nums: list[int], k: int) -> int:
    max_window = 0
    num_zeros = 0
    n = len(nums)
    left = 0
    for right in range(n):
        if nums[right] == 0:
            num_zeros += 1
        while num_zeros > k:
            if nums[left] == 0:
                num_zeros -= 1
            left += 1
        max_window = max(max_window, right - left + 1)
    return max_window


class TestLongestOnes(unittest.TestCase):
    def test1(self):
        nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
        k = 2
        self.assertEqual(6, longest_ones(nums, k))

    def test2(self):
        nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
        k = 3
        self.assertEqual(10, longest_ones(nums, k))
