"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

"""
思路：从上至下维护一个2d 数组，
dp[i][j]代表是移动到grid[i][j]时的最小值
dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
其中注意两种情况，当i=0的时候，dp只能从左边取值（即dp第一行是grid第一行从左至右的累加）；当j=0的时候dp只能从上面取值
"""


def solve(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for i in range(m)]

    for i in range(n):
        dp[0][i] = dp[0][max(i-1, 0)] + grid[0][i]

    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[-1][-1]


if __name__ == '__main__':
    assert solve([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert solve([[1, 2, 3], [4, 5, 6]]) == 12
