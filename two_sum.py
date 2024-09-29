import unittest


def two_sum(nums, target):
    cache = {}
    for i in range(len(nums)):
        if target - nums[i] in cache.keys():
            return [i, cache[target - nums[i]]]
        else:
            cache[nums[i]] = i


class TestTwoSum(unittest.TestCase):
    def test_two_sum1(self):
        nums = [2, 7, 11, 15]
        target = 9
        result = two_sum(nums, target)
        self.assertTrue(result == [0, 1] or result == [1, 0])

    def test_two_sum2(self):
        nums = [3, 2, 4]
        target = 6
        result = two_sum(nums, target)
        self.assertTrue(result == [1, 2] or result == [2, 1])

    def test_two_sum3(self):
        nums = [3, 3]
        target = 6
        result = two_sum(nums, target)
        self.assertTrue(result == [0, 1] or result == [1, 0])



