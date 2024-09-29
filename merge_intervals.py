import unittest


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda interval: interval[0])
    res = []
    for interval in intervals:
        if len(res) != 0 and res[-1][1] >= interval[0]:
            res[-1] = [res[-1][0], max(res[-1][1], interval[1])]
        else:
            res.append(interval)
    return res


class TestMerge(unittest.TestCase):
    def test_merge1(self):
        intervals = [[1,3],[8,10],[2,6],[15,18]]
        output = [[1,6],[8,10],[15,18]]
        self.assertEqual(output, merge_intervals(intervals))

    def test_merge2(self):
        intervals = [[1,4],[4,5]]
        output = [[1,5]]
        self.assertEqual(output, merge_intervals(intervals))
