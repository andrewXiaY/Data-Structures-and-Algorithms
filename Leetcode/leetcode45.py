# This problem called jump game II
"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.
"""
# 一句话，我们需要找到当前可走区间中，下一次jump能够抵达的最远位置


def jump(arr: [int]):
    size = len(arr)

    if size <= 1:
        return 0

    # the max position we can arrive starting from any position where we can go from current position
    max_position = arr[0]
    max_steps = arr[0]  # the max steps we can go from current position
    ans = 1

    for i in range(size):
        # if i is larger than the max steps, we should jump one more time,
        # and the next max steps should be the max position we can go starting from index <= i
        if max_steps < i:
            ans += 1
            max_steps = max_position

        max_position = max(arr[i] + i, max_position)