# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

"""
dp[i][j] 代表以i，j为右下端点的square有多少个，当mat[i][j] == 0时dp[i][j] = 0
当mat[i][j] == 1 时dp[i][j] = min(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j]) + 1
因为如果mat[i][j]能都作为一个正方形的端点，那么说明其mat[i][j], mat[i-1][j-1], mat[i-1][j], mat[i][j-1]都是1，并且其都能成为正方形
的端点，我们只需要取最小值 + 1即可
"""


def solve(mat):

    m, n = len(mat), len(mat[0])

    ans = 0
    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        if mat[i][0] == 1:
            dp[i][0] = 1
            ans += 1

    for j in range(1, n):
        if mat[0][j] == 1:
            dp[0][j] = 1
            ans += 1

    for i in range(1, m):
        for j in range(1, n):
            if mat[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                ans += dp[i][j]

    return ans