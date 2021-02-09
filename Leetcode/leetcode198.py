"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.

"""


"""
思路：非常简单的思路，就是回溯两个单位，也就是决定偷不偷当前位置i，如果偷当前位置则不能偷i-1，如果不偷当前i，则能偷i-1位置
比较这两种情况即可
"""


def solve(nums):
    n = len(nums)
    if n == 0:
        return 0
    elif n == 1:
        return nums[0]

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[:2])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[-1]