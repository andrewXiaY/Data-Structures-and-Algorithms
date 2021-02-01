# There is a fence with n posts, each post can be painted with one of the k colors.
#
# You have to paint all the posts such that no more than two adjacent fence posts have the same color.
#
# Return the total number of ways you can paint the fence.
#
# Note:
# n and k are non-negative integers.
#
# Example:
#
# Input: n = 3, k = 2
# Output: 6
# Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:
#
#             post1  post2  post3
#  -----      -----  -----  -----
#    1         c1     c1     c2
#    2         c1     c2     c1
#    3         c1     c2     c2
#    4         c2     c1     c1
#    5         c2     c1     c2
#    6         c2     c2     c1


# By induction, we can get f(n) = (k - 1) (f(n - 1) + f(n - 2))
"""
只有两种情况：
第一：第i个post和第i-1个相同颜色 (k - 1) * f(i - 2) (因为颜色相同那么第i-2个肯定和i，i-1不同)
第二：第i个post和第i-1个不同颜色 (k - 1) * f(i - 1)
"""


def solve(n, k):
    if n == 0 or k == 0:
        return 0
    dp = [k, k*k] + [0] * (n - 1)
    for i in range(2, n):
        dp[i] = (k-1) * (dp[i-1] + dp[i-2])
    return dp[n-1]



