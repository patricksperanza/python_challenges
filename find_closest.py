import unittest


def find_closest(nums):
    closest = nums[0]
    for num in nums:
        if abs(num) < abs(closest):
            closest = num
    if closest < 0 and abs(closest) in nums:
        return abs(closest)
    return closest


class TestFindClosest(unittest.TestCase):
    def test_find_closest(self):
        nums = [-4, -2, 1, 4, 8]
        self.assertEqual(1, find_closest(nums))

    def test_find_closest2(self):
        nums = [2, -1, 1]
        self.assertEqual(1, find_closest(nums))

