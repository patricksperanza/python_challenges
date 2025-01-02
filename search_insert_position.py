import unittest


def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    mid = (left + right) // 2
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1

    if nums[mid] < target:
        return mid + 1
    else:
        return mid


class TestSearchInsertPosition(unittest.TestCase):
    def test_search1(self):
        nums = [-1, 0, 3, 5, 9, 12]
        self.assertEqual(4, search(nums, 9))

    def test_search2(self):
        nums = [-1, 0, 3, 5, 9, 12]
        self.assertEqual(2, search(nums, 2))

