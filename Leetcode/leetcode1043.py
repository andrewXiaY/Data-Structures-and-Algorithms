# Given an integer array arr, you should partition the array into (contiguous) subarrays of length at most k.
# After partitioning, each subarray has their values changed to become the maximum value of that subarray.

# Return the largest sum of the given array after partitioning.

"""
思路：
使用dp[i]代表arr[0:i] 的结果
对于k而言，我们可以遍历1到k，使用之前计算过的结果来得到答案

--- --- --- --- ----- ----- --- --- ---
 1 | 2 | 3 |...| i-k |i-k+1|...|i-1| i
--- --- --- --- ----- ----- --- --- ---

对于i而言，我们可以计算dp[i-j] + max(arr[i-j+1:i]) * j （其中 1 <= j <= k） 的最大值即可
"""


def solve(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        c_max = float("-inf")
        for j in range(1, min(k, i) + 1):
            c_max = max(c_max, arr[i - j])
            dp[i] = max(dp[i], dp[i - j] + c_max * j)
    return dp[-1]


if __name__ == '__main__':
    assert solve([1,4,1,5,7,3,6,1,9,9,3], 4) == 83

