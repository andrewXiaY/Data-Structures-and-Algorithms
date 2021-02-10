"""
We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average of
each group. What is the largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily integers.
"""


def solve(A, K) -> float:
    sums = [0]
    for c in A:
        sums.append(sums[-1] + c)

    def average(i, j):
        return (sums[j] - sums[i]) / (j - i)

    n = len(A)

    dp = [average(i, n) for i in range(n)]

    # 迭代K - 1次
    for _ in range(K - 1):
        for i in range(n):
            for j in range(i + 1, n):
                dp[i] = max(dp[i], average(i, j) + dp[j])
    return dp[0]


if __name__ == '__main__':
    assert solve([9, 1, 2, 3, 9], 3) == 20
