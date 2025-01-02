import unittest


def trap(height):
    l_wall = 0
    r_wall = 0
    n = len(height)
    max_left = [0] * n
    max_right = [0] * n
    for i in range(n):
        j = -i - 1
        max_left[i] = l_wall
        max_right[j] = r_wall
        l_wall = max(l_wall, height[i])
        r_wall = max(r_wall, height[j])

    summ = 0
    for i in range(n):
        pot = min(max_left[i], max_right[i])
        summ += max(0, pot - height[i])
    return summ


class TestTrap(unittest.TestCase):
    def test_trap1(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        self.assertEqual(6, trap(height))

    def test_trap2(self):
        height = [4, 2, 0, 3, 2, 5]
        self.assertEqual(9, trap(height))
