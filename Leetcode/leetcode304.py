"""
range sum query 2d
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner
(row1, col1) and lower right corner (row2, col2).
"""

"""
思路：和求range sum一样，就是几个小块相互加减
"""


class NumMatrix:
    def __init__(self, matrix):
        self.total_sum = self._sum(matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        row2 += 1
        col1 += 1
        col2 += 1
        return self.total_sum[row2][col2] - self.total_sum[row1 - 1][col2] - self.total_sum[row2][col1 - 1] + \
               self.total_sum[row1 - 1][col1 - 1]

    def _sum(self, matrix):
        if not matrix:
            return [[[]]]
        m, n = len(matrix), len(matrix[0])

        sums = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sums[i][j] = sums[i - 1][j] + sums[i][j - 1] - sums[i - 1][j - 1] + matrix[i - 1][j - 1]
        return sums
