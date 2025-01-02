import unittest


def jewels_in_stones(jewels, stones):
    return len([s for s in stones if s in jewels])


class TestJewelsInStones(unittest.TestCase):
    def test_jewels1(self):
        jewels = "aA"
        stones = "aAAbbbb"
        self.assertEqual(3, jewels_in_stones(jewels, stones))

    def test_jewels2(self):
        jewels = "z"
        stones = "ZZ"
        self.assertEqual(0, jewels_in_stones(jewels, stones))
