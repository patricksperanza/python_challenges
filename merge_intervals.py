import unittest


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda i: i[0])
    merged = []
    for interval in intervals:
        if merged and merged[-1][1] >= interval[0]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)
    return merged


class TestMerge(unittest.TestCase):
    def test_merge1(self):
        intervals = [[1, 3], [8, 10], [2, 6], [15, 18]]
        output = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(output, merge_intervals(intervals))

    def test_merge2(self):
        intervals = [[1, 4], [4, 5]]
        output = [[1, 5]]
        self.assertEqual(output, merge_intervals(intervals))
