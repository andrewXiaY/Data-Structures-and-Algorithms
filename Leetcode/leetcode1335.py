# Hard Problem
"""
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the i-th job, you have to finish all
the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day
of the d days. The difficulty of a day is the maximum difficulty of a job done in that day.

Given an array of integers jobDifficulty and an integer d. The difficulty of the i-th job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.
"""


def solve(jobDifficulty, d):
    n = len(jobDifficulty)
    # 如果时间数大于工作数，总会有至少一天无法岸安排工作
    if d > n:
        return -1

    dp = [[float('inf')] * (d + 1) for _ in range(n+1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for k in range(1, d + 1):
            md = 0
            for j in range(i - 1, k - 2, -1):
                md = max(md, jobDifficulty[j])
                dp[i][k] = min(dp[i][k], dp[j][k - 1] + md)

    return dp[n][d]


if __name__ == '__main__':
    assert solve([6, 5, 4, 3, 2, 1], 2) == 7
