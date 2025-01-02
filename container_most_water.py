import unittest


def max_area(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    res = 0
    while left < right:
        width = right - left
        min_height = min(height[left], height[right])
        area = width*min_height
        res = max(res, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return res


class TestMostWater(unittest.TestCase):
    def test_most1(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        self.assertEqual(49, max_area(height))

    def test_most2(self):
        height = [1, 1]
        self.assertEqual(1, max_area(height))
