import unittest


def num_islands(grid: list[list[str]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    def dfs(i: int, j: int) -> None:
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != "1":
            return
        else:
            grid[i][j] = "0"
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

    islands = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                islands += 1
                dfs(i, j)
    return islands


class TestNumberOfIslands(unittest.TestCase):
    def test1(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        self.assertEqual(1, num_islands(grid))

    def test2(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        self.assertEqual(3, num_islands(grid))
