import unittest


def find_min(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1
    return nums[left]


class TestFindMin(unittest.TestCase):
    def test_find_min1(self):
        nums = [3, 4, 5, 1, 2]
        self.assertEqual(1, find_min(nums))

    def test_find_min2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        self.assertEqual(0, find_min(nums))

    def test_find_min3(self):
        nums = [11, 13, 15, 17]
        self.assertEqual(11, find_min(nums))

    def test_find_min4(self):
        nums = [25, 27, 12, 13, 17, 22, 23]
        self.assertEqual(12, find_min(nums))

    def test_find_min5(self):
        nums = [10, 11, 12, 13, 14, 15, 9]
        self.assertEqual(9, find_min(nums))

