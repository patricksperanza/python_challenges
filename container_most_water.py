import unittest


def max_area(height: list[int]) -> int:
    n = len(height)
    left = 0
    right = n - 1
    result = 0
    while left < right:
        w = right - left
        h = min(height[left], height[right])
        area = w * h
        result = max(result, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return result


class TestMostWater(unittest.TestCase):
    def test_most1(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        self.assertEqual(49, max_area(height))

    def test_most2(self):
        height = [1, 1]
        self.assertEqual(1, max_area(height))
