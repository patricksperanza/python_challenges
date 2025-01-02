import unittest


def search(nums: list[int], target: int) -> int:
    n = len(nums)
    left = 0
    right = n - 1
    while left < right:
        m = (left + right) // 2
        if nums[m] < nums[right]:
            right = m
        else:
            left = m + 1
    min_index = left
    if min_index == 0:
        left = 0
        right = n - 1
    elif nums[0] <= target <= nums[min_index - 1]:
        left = 0
        right = min_index - 1
    else:
        left = min_index
        right = n - 1

    while left <= right:
        m = (left + right) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            left = m + 1
        else:
            right = m - 1
    return - 1


class TestSearchRotatedSortedArray(unittest.TestCase):
    def test1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        self.assertEqual(4, search(nums, target))

    def test2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        self.assertEqual(-1, search(nums, target))
