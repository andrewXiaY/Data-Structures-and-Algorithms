"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted
without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is
not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.
"""

"""
思路：相当于是原题，就是从后往前dp
"""


def solve(text1: str, text2: str) -> int:
    m = len(text1)
    n = len(text2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1

            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    return dp[0][0]