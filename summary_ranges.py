import unittest


def summary_ranges(nums: list[int]) -> list[str]:
    i = 0
    res = []
    while i < len(nums):
        first = nums[i]
        while i < len(nums) - 1 and nums[i+1] == nums[i] + 1:
            i += 1
        last = nums[i]
        if first == last:
            res.append(str(first))
        else:
            res.append(f"{first}->{last}")
        i += 1
    return res


class TestSummary(unittest.TestCase):
    def test_1(self):
        nums = [0, 1, 2, 4, 5, 7]
        self.assertEqual(["0->2", "4->5", "7"], summary_ranges(nums))

    def test_2(self):
        nums = nums = [0, 2, 3, 4, 6, 8, 9]
        self.assertEqual(["0", "2->4", "6", "8->9"], summary_ranges(nums))