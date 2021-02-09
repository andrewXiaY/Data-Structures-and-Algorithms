"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -.
For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.
"""

"""
个人感觉是一个非常经典的dp问题，知道思路后挺简单的
"""


def brute_force(nums, s):
    n = len(nums)
    counts = 0

    def calculate(start, cur_sum):
        nonlocal counts

        if start == n:
            if cur_sum == s:
                counts += 1

        else:
            calculate(start + 1, cur_sum + nums[start])
            calculate(start + 1, cur_sum - nums[start])

    calculate(0, 0)

    return counts


def dynamic_programming(nums, s):
    n = len(nums)
    l = sum(nums)

    if s > 1000 or l < s:
        return 0

    # 模拟可能出现的sum的范围
    # dp[i][j] 表示到第i个数，sum为j的可能个数
    # dp[i][j + nums[i]] += dp[i-1][j]
    # dp[i][j - nums[i]] += dp[i-1][j]
    # 需要特殊处理下第二个维度的index，因为sum可能存在负数
    dp = [[0] * (2 * l + 1) for _ in range(n)]

    dp[0][nums[0] + l] = 1
    dp[0][-nums[0] + l] += 1

    for i in range(1, n):
        for j in range(-l, l):
            if dp[i-1][j + l] > 0:
                dp[i][j+l+nums[i]] += dp[i-1][j+l]
                dp[i][j+l-nums[i]] += dp[i-1][j+l]

    return dp[-1][s+l]


if __name__ == '__main__':
    assert dynamic_programming([1, 1, 1, 1, 1], 3) == 5
    assert brute_force([1, 1, 1, 1, 1], 3) == 5

