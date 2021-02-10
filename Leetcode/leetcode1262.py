"""
Given an array nums of integers, we need to find the maximum possible sum of elements of the array
such that it is divisible by three.
"""

"""
思路很奇妙，我暂时也不能完全理解，
"""


def solve(nums):
    dp = [0, 0, 0]

    for n in nums:
        t_dp = dp[:]
        for i in range(len(dp)):
            c_sum = t_dp[i] + n
            dp[c_sum % 3] = max(dp[c_sum % 3], c_sum)

    return dp[0]


if __name__ == '__main__':
    assert solve([3, 6, 5, 1, 8]) == 18
