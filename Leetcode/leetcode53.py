# 简单题
# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
# 贪心算法


def solve(nums):
    cur_sum = max_sum = nums[0]
    for c in nums[1:]:
        cur_sum = max(c, c + cur_sum)
        max_sum = max(max_sum, cur_sum)

    return max_sum
