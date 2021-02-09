"""
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].


Note:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
"""

"""
思路：两个字符串，考察A_i and B_j的最长的公有前缀，我最开始只考虑单个字符串，所以想不出来
如果考虑了最长公有前缀的话，dp[i][j] = dp[i+1][j+1] + 1 if A[i] == B[j],
而且从后往前遍历
"""


def solve(A, B):
    n, m = len(A), len(B)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if A[i] == B[j]:
                dp[i][j] = dp[i+1][j+1] + 1
    return max(max(row) for row in dp)


if __name__ == '__main__':
    assert solve([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]) == 3

