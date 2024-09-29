import unittest


def calc_points(operations: list[str]) -> int:
    rec = []
    for op in operations:
        if op == "+":
            rec.append(rec[-1] + rec[-2])
        elif op == "D":
            rec.append(rec[-1] * 2)
        elif op == "C":
            rec.pop()
        else:
            rec.append(int(op))
    return sum(rec)


class TestCalcPoints(unittest.TestCase):
    def test_calc1(self):
        ops = ["5", "2", "C", "D", "+"]
        self.assertEqual(30, calc_points(ops))

    def test_calc2(self):
        ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
        self.assertEqual(27, calc_points(ops))

    def test_calc3(self):
        ops = ["1", "C"]
        self.assertEqual(0, calc_points(ops))

