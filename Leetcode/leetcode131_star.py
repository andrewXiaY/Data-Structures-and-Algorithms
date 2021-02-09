"""
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.



Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]


Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.

"""

"""
思路：关键是使用dfs的方式得到结果
从i开始到n，看i -> j是不是一个回文，如果是回文的话就将其加入到当前list中，然后继续从j + 1开始继续dfs
"""

from copy import deepcopy

def isPalindrome(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        else:
            start += 1
            end -= 1
    return True


def dfs(s, start, cur_list, result):
    if start >= len(s):
        result.append(deepcopy(cur_list))

    for end in range(start, len(s)):
        if isPalindrome(s, start, end):
            cur_list.append(s[start:end + 1])
            dfs(s, end + 1, cur_list, result)
            cur_list.pop(-1)


def solve(s):
    result = []
    dfs(s, 0, [], result)
    return result
