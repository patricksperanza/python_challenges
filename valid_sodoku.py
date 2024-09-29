import unittest


def is_valid(board: list[list[str]]) -> bool:
    for i in range(len(board)):
        s = set()
        for j in range(len(board[0])):
            item = board[i][j]
            if item in s:
                return False
            elif item != ".":
                s.add(item)

    for i in range(len(board)):
        s = set()
        for j in range(len(board[0])):
            item = board[j][i]
            if item in s:
                return False
            elif item != ".":
                s.add(item)
    starts = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    for i, j in starts:
        s = set()
        for row in range(i, i + 3):
            for col in range(j, j+3):
                item = board[row][col]
                if item in s:
                    return False
                elif item != ".":
                    s.add(item)
    return True


class TestIsValid(unittest.TestCase):
    def test_is_valid1(self):
        board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."],
                 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."],
                 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        self.assertTrue(is_valid(board))

    def test_is_valid2(self):
        board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."],
                 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."],
                 [".", "1", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        self.assertFalse(is_valid(board))
