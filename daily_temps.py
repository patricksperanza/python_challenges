import unittest


def daily_temperatures(temps: list[int]) -> list[int]:
    n = len(temps)
    stk = []
    ans = [0] * n
    for i, t in enumerate(temps):
        while stk and stk[-1][0] < t:
            st, si = stk.pop()
            ans[si] = i - si
        stk.append((t, i))
    return ans


class TestDailyTemps(unittest.TestCase):
    def test_temps1(self):
        inp = [73, 74, 75, 71, 69, 72, 76, 73]
        output = daily_temperatures(inp)
        expected = [1, 1, 4, 2, 1, 1, 0, 0]
        self.assertEqual(expected, output)

    def test_temps2(self):
        inp = [30, 40, 50, 60]
        output = daily_temperatures(inp)
        expected = [1, 1, 1, 0]
        self.assertEqual(expected, output)

    def test_temps3(self):
        inp = [30, 60, 90]
        output = daily_temperatures(inp)
        expected = [1, 1, 0]
        self.assertEqual(expected, output)
