"""
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets
such that the sum of elements in both subsets is equal.
"""


"""
思路：
1. 先求总和，用总和除2得到每个subset和是多少 (假设是sub_sum)
2. 使用一个2d数组来记录是否能用前i个数加得数j （这里j <= sub_sum）

dp[i][j] = True, 当dp[i-1][j]也是true，或者dp[i-1][j - nums[i]] 为true

这里很巧妙的使用了不同的两个维度，这是需要学习的
"""


def solve(nums):
    total = sum(nums)
    sub_sum = total // 2
    n = len(nums)

    if total % 2 != 0:
        return False

    dp = [[False] * (sub_sum + 1) for _ in range(n + 1)]

    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(1, sub_sum + 1):
            if j < nums[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]

    return dp[n][sub_sum]

# 还有一种使用深度优先的方式， 思路是从sub_sum中逐个减去当前值（也可以不减去，直接将需要考虑的nums范围减一），然后看剩余的数是否为0，这两种
# 情况只要有一个为真即为真


if __name__ == '__main__':
    assert solve([1, 5, 11, 5])
