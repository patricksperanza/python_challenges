import unittest


def summary_ranges(nums: list[int]) -> list[str]:
    n = len(nums)
    if n == 0:
        return []
    elif n == 1:
        return [str(nums[0])]
    res = []
    i = 0
    j = 1
    while i < n and j < n:
        s = [str(nums[i])]
        sequence = False
        while j < n and nums[j] == nums[i] + 1:
            sequence = True
            i += 1
            j += 1
        if sequence:
            s.append('->' + str(nums[i]))
        res.append("".join(s))
        i += 1
        j += 1
    if i < n:
        res.append(str(nums[i]))
    return res


class TestSummary(unittest.TestCase):
    def test_1(self):
        nums = [0, 1, 2, 4, 5, 7]
        self.assertEqual(["0->2", "4->5", "7"], summary_ranges(nums))

    def test_2(self):
        nums = [0, 2, 3, 4, 6, 8, 9]
        self.assertEqual(["0", "2->4", "6", "8->9"], summary_ranges(nums))

    def test_3(self):
        nums = [1]
        self.assertEqual(["1"], summary_ranges(nums))

    def test_4(self):
        nums = []
        self.assertEqual([], summary_ranges(nums))

