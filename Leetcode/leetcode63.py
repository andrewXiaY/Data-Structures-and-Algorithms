"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.
"""

"""
思路：
比较基础的一道题，关键是判断边界的情况，棋盘内部情况能够通过
dp[i][j] = dp[i-1][j] + dp[i][j-1] if grid[i][j] == 0 来计算
边界情况：对于dp[i][0] or dp[0][j]，其实就是判断dp[i-1][0] and dp[0][j-1]是否是1并且grid[i][0] and grid[0][j]不为1（不是障碍物）
"""


def solve(grid):
    m, n = len(grid), len(grid[0])

    dp = [[0] * n for _ in range(m)]

    dp[0][0] = 1 if grid[0][0] == 0 else 0

    for i in range(1, n):
        if grid[0][i] == 1 or dp[0][i-1] == 0:
            dp[0][i] = 0
        else:
            dp[0][i] = 1

    for i in range(1, m):
        if grid[i][0] == 1 or dp[i-1][0] == 0:
            dp[i][0] = 0
        else:
            dp[i][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] != 1:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]


if __name__ == '__main__':
    assert solve([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
