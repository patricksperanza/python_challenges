import unittest


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    height = len(matrix)
    width = len(matrix[0])
    left = 0
    right = height * width - 1

    while left <= right:
        mid = (left + right) // 2
        i = mid // width
        j = mid % width
        mid_num = matrix[i][j]
        if mid_num == target:
            return True
        elif mid_num < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


class TestSearchMatrix(unittest.TestCase):
    def test_search_matrix1(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 3
        self.assertTrue(search_matrix(matrix, target))

    def test_search_matrix2(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 13
        self.assertFalse(search_matrix(matrix, target))
