import math
import unittest


def min_eating_speed(piles: list[int], h: int) -> int:
    def rate_works(rate):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / rate)
        return hours <= h

    left = 1
    right = max(piles)
    while left < right:
        k = (left + right) // 2
        if rate_works(k):
            right = k
        else:
            left = k + 1
    return right


class TestKokoEatingBananas(unittest.TestCase):
    def test1(self):
        piles = [3, 6, 7, 11]
        hours = 8
        self.assertEqual(4, min_eating_speed(piles, hours))

    def test2(self):
        piles = [30, 11, 23, 4, 20]
        hours = 5
        self.assertEqual(30, min_eating_speed(piles, hours))

    def test3(self):
        piles = [30, 11, 23, 4, 20]
        hours = 6
        self.assertEqual(23, min_eating_speed(piles, hours))
