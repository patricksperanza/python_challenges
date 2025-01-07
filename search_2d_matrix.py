import unittest


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    left = 0
    right = num_rows * num_cols - 1
    while left <= right:
        mid = (left + right) // 2
        cur_row = mid // num_cols
        cur_col = mid % num_cols
        if matrix[cur_row][cur_col] == target:
            return True
        elif matrix[cur_row][cur_col] < target:
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
