import unittest


def find_min_index(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1
    return left


def binary_search(nums: list[int], target: int, left: int, right: int) -> int:
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def search(nums: list[int], target: int) -> int:
    min_index = find_min_index(nums)
    left = 0
    right = len(nums) - 1
    if target <= nums[right]:
        left = min_index
    else:
        right = min_index - 1
    return binary_search(nums, target, left, right)


class TestSearchRotatedSortedArray(unittest.TestCase):
    def test1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        self.assertEqual(4, search(nums, target))

    def test2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        self.assertEqual(-1, search(nums, target))

    def test3(self):
        nums = [1]
        target = 0
        self.assertEqual(-1, search(nums, target))

    def test4(self):
        nums = [3, 1]
        target = 3
        self.assertEqual(0, search(nums, target))