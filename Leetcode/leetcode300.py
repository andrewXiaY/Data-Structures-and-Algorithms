"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order
of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""

"""
思路：很简单，使用一个1d数组维护到第i个元素时最长的是多少
dp[i] = max(dp[j] + 1) where 0 <= j < i and nums[i] > nums[j] 
"""


def solve(nums):
    n = len(nums)
    dp = [1] * n
    longest = 1
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                longest = max(longest, dp[i])

    return longest


if __name__ == '__main__':
    assert solve([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert solve([0, 1, 0, 3, 2, 3]) == 4







