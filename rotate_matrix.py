import unittest


def rotate_matrix(mat):
    n = len(mat)
    for i in range(n):
        for j in range(i+1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    for i in range(n):
        for j in range(n // 2):
            mat[i][j], mat[i][n-j-1] = mat[i][n-j-1], mat[i][j]
    return mat


class TestRotate(unittest.TestCase):
    def test_rotate1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        output = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        self.assertEqual(output, rotate_matrix(matrix))

    def test_rotate2(self):
        matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        output = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        self.assertEqual(output, rotate_matrix(matrix))
