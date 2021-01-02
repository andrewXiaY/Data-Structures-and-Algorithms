# Is subsequence

# Given a string s and a string t, check if s is subsequence of t.

# A subsequence of a string is a new string which is formed from the original string
# by deleting some (can be none) of the characters without disturbing the relative
# positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).
# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by
# one to see if T has its subsequence. In this scenario, how would you change your code?

def solve(s, t):
    cur_pos = 0
    for c in t:
        if cur_pos < len(s) and c == s[cur_pos]:
            cur_pos += 1

    return cur_pos == len(s)