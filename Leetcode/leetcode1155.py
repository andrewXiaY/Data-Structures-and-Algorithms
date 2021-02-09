"""
You have d dice, and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up
numbers equals target.
"""


def solve(d, f, target):
    dp = [[0] * 1001 for _ in range(d)]

    for i in range(1, f + 1):
        dp[0][i] = 1

    for i in range(1, d):
        for j in range(i, min((i + 1)*f + 1, target + 1)):
            for k in range(1, f+1):
                dp[i][j] = (dp[i][j] + dp[i-1][j-k]) % (1e9 + 7)

    return dp[-1][target]


if __name__ == '__main__':
    assert solve(30, 30, 500) == 222616187
    assert solve(1, 2, 3) == 0

