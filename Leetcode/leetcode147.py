"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same
characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Note:

The input string length won't exceed 1000.
"""


"""
其实就是找回文，回文的两种方式, 遍历字符串，从每一个点算回文
"""


def solve(s):
    n = len(s)
    ans = 0
    for i in range(n):
        left, right = i, i
        # 中心对称
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
            ans += 1
        # 轴对称
        left, right = i, i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
            ans += 1

    return ans
