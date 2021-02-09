"""
Given a string s, find the longest palindromic subsequence's length in s.
You may assume that the maximum length of s is 1000.
"""

"""
思路：
参考leetcode718
将字符串reverse，然后找最长子串 
"""


def solve(s):
    rev_s = s[-1::-1]
    n = len(rev_s)

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if s[i] == rev_s[j]:
                dp[i][j] = dp[i+1][j+1] + 1
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])

    return dp[0][0]


if __name__ == "__main__":
    assert solve("bbbab") == 4

