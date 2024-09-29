import unittest


def max_profit(prices):
    min_price = prices[0]
    max_prof = 0
    for i in range(1, len(prices)):
        max_prof = max(max_prof, prices[i] - min_price)
        min_price = min(min_price, prices[i])
    return max_prof


class TestMaxProfit(unittest.TestCase):
    def test_max_profit1(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(5, max_profit(prices))

    def test_max_profit2(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(0, max_profit(prices))
