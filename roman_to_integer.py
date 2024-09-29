import unittest


def roman_to_int(s):
    m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = m[s[-1]]
    for i in range(len(s) - 1):
        if m[s[i]] < m[s[i+1]]:
            res -= m[s[i]]
        else:
            res += m[s[i]]
    return res


class TestRomanToInteger(unittest.TestCase):
    def test_1(self):
        s = "III"
        self.assertEqual(3, roman_to_int(s))

    def test_2(self):
        s = "MCMXCIV"
        self.assertEqual(1994, roman_to_int(s))

    def test_3(self):
        s = "LVIII"
        self.assertEqual(58, roman_to_int(s))