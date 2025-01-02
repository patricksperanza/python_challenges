import unittest


def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    ans = []
    n = len(nums)
    for i in range(n):
        if nums[i] > 0:
            break
        elif i > 0 and nums[i] == nums[i-1]:
            continue
        lo, hi = i + 1, n - 1
        while lo < hi:
            summ = nums[i] + nums[lo] + nums[hi]
            if summ == 0:
                ans.append([nums[i], nums[lo], nums[hi]])
                lo, hi = lo + 1, hi - 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
                while lo < hi and nums[hi] == nums[hi + 1]:
                    hi -= 1
            elif summ < 0:
                lo += 1
            else:
                hi -= 1
    return ans


class TestThreeSum(unittest.TestCase):
    def test_three_sum1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        output = three_sum(nums)
        self.assertEqual(2, len(output))
        self.assertTrue([-1, -1, 2] in output)
        self.assertTrue([-1, 0, 1] in output)

    def test_three_sum2(self):
        nums = [0, 1, 1]
        output = three_sum(nums)
        self.assertEqual(0, len(output))

    def test_three_sum3(self):
        nums = [0, 0, 0]
        output = three_sum(nums)
        self.assertEqual(1, len(output))
        self.assertTrue([0, 0, 0] in output)
