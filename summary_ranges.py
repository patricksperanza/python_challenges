import unittest

"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""


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