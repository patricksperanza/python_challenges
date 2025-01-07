import unittest


def insertion_sort(nums: list[int]) -> None:
    for i in range(1, len(nums)):
        cur = nums[i]
        j = i
        while j > 0 and nums[j - 1] > cur:
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = cur


class TestInsertionSort(unittest.TestCase):
    def test1(self):
        nums = [5, 2, 4, 1, 0, 6, 8, 7, 3]
        insertion_sort(nums)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8], nums)

    def test2(self):
        nums = [3, 2, 1, -5]
        insertion_sort(nums)
        self.assertEqual([-5, 1, 2, 3], nums)

    def test3(self):
        nums = []
        insertion_sort(nums)
        self.assertEqual([], nums)
