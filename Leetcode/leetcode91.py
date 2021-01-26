"""

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be mapped back into letters using the reverse of the mapping
above (there may be multiple ways). For example, "111" can have each of its "1"s be mapped into 'A's to make
"AAA", or it could be mapped to "11" and "1" ('K' and 'A' respectively) to make "KA". Note that "06" cannot be
mapped into 'F' since "6" is different from "06".

Given a non-empty string num containing only digits, return the number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.
"""

"""
使用动态规划的思想：
设P(i)是s[:i+1]能被decode的方式数目，那我们可以知道
P(i) = P(i - 1) 如果第i个字符不为0，并且如果s[i-1:i+1]在10到26之间，那么P(i) = P(i-1) + P(i-2)
还有一种特殊情况是当s[i] == 0, 并且前一个字符不是1或者2，则这个字符串能被decode的方式为0
"""


def solve(s):
    dp = [0] * (len(s) + 1)
    dp[0] = 1
    dp[1] = 0 if s[0] == '0' else 1  # 如果首字符为0，那么dp[1] = 0这个里面的index比字符所在index要大1

    for i in range(2, len(dp)):
        if s[i - 1] != '0':
            dp[i] = dp[i - 1]

        two_digit = int(s[i-2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i-2]

    return dp[-1]

