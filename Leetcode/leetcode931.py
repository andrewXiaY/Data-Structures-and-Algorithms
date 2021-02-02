# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

# A falling path starts at any element in the first row and chooses the element in the next row that is either directly
# below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1),
# (row + 1, col), or (row + 1, col + 1).

"""
思路：
dp[i][j]代表当fail到matrix[i][j]位置上时最小的sum是多少，那么全局的最小sum就只需要对最后一列取最小值即可
dp[i][j] = min(dp[i-1][j-1:j+2]) + matrix[i][j]
"""


def solve(matrix):
    n = len(matrix)
    # 可以使用一个2d数组维护dp，也可以inplace
    while len(matrix) >= 2:
        row = matrix.pop()
        for i in range(len(row)):
            matrix[-1][i] += min(row[max(i-1, 0): min(i + 1, n - 1) + 1])

    return min(matrix[0])


if __name__ == '__main__':
    assert solve([[2, 1, 3], [6, 5, 4], [7, 8, 9]]) == 13

