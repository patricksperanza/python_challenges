import unittest


def spiral(matrix: list[list[int]]) -> list[int]:
    left = 0
    top = 0
    right = len(matrix[0])
    bottom = len(matrix)
    res = []
    while left < right and top < bottom:
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1
        for i in range(top, bottom):
            res.append(matrix[i][right-1])
        right -= 1

        if not (left < right and top < bottom):
            break

        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom-1][i])
        bottom -= 1
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        left += 1
    return res






class TestSpiral(unittest.TestCase):
    def test_spiral1(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        output = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        self.assertEqual(output, spiral(matrix))

    def test_spiral2(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        output = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(output, spiral(matrix))
