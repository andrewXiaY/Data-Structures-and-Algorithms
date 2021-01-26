# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

"""
先计算每个字符出现的次数，然后从左至右遍历字符串，如果某个字符只出现过一次就返回这个字符
"""
from collections import Counter


def solve(s):
    counts = Counter(s)
    for ind, c in enumerate(s):
        if counts[c] == 1:
            return ind
    return -1
