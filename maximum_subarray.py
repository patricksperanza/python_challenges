import unittest


def max_subarray(nums):
    current_sum = 0
    max_sum = float('-inf')
    for num in nums:
        current_sum = max(current_sum + num, num)
        max_sum = max(max_sum, current_sum)
    return max_sum


class TestMaxSubarray(unittest.TestCase):
    def testMaxSubarray1(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(6, max_subarray(nums))

    def testMaxSubarray2(self):
        nums = [1]
        self.assertEqual(1, max_subarray(nums))

    def testMaxSubarray3(self):
        nums = [5, 4, -1, 7, 8]
        self.assertEqual(23, max_subarray(nums))

    def testMaxSubarray4(self):
        nums = [-5, -8]
        self.assertEqual(-5, max_subarray(nums))

