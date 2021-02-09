"""
Given an array A of integers, return the length of the longest arithmetic subsequence in A.

Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1,
and that a sequence B is arithmetic if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).
"""


"""
思路：
dp[i]存着第i个数对 0 -> (i-1)个数的差，并且记录了最长的arithmetic subsequence的长度

nums[i] - nums[j] 在dp[j]中如果存在，那么dp[i][nums[i] - nums[j]] = dp[j][delta] + 1

这是怎么想到的呢？我想不到
"""


def solve(nums):
    n = len(nums)
    dp = [{} for _ in range(n)]

    m = 0

    for i in range(n):
        for j in range(i):
            delta = nums[i] - nums[j]

            if delta in dp[j]:
                cur = dp[j][delta] + 1
                dp[i][delta] = cur

            else:
                dp[i][delta] = 2

            m = max(dp[i][delta], m)

    return m

