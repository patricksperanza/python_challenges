import unittest


def two_sum(nums: list[int], target: int) -> list[int]:
    left = 0
    right = len(nums) - 1
    while left < right:
        summ = nums[left] + nums[right]
        if summ == target:
            return [left + 1, right + 1]
        elif summ < target:
            left += 1
        else:
            right -= 1


class TestTwoSumSorted(unittest.TestCase):
    def test1(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual([1, 2], two_sum(nums, target))

    def test2(self):
        nums = [2, 3, 4]
        target = 6
        self.assertEqual([1, 3], two_sum(nums, target))

    def test3(self):
        nums = [-1, 0]
        target = -1
        self.assertEqual([1, 2], two_sum(nums, target))
