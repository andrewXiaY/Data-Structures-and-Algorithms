# count sorted vowel strings

# Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u)
# and are lexicographically sorted.

# A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

# Example 1:
#
# Input: n = 1
# Output: 5
# Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
# Example 2:
#
# Input: n = 2
# Output: 15
# Explanation: The 15 sorted strings that consist of vowels only are
# ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
# Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
# Example 3:
#
# Input: n = 33
# Output: 66045


def solve(n, vowel, dp):
    if n == 1:
        return vowel
    if vowel == 1:
        return 1
    if dp[n][vowel] != 0:
        return dp[n][vowel]

    dp[n][vowel] = solve(n - 1, vowel, dp) + solve(n, vowel - 1, dp)
    return dp[n][vowel]


def count_vowel_strings(n):
    dp = [[0] * 6 for _ in range(n + 1)]
    return solve(n, 5, dp)


# 方法2
def solve2(n):
    dp = [1] * 5
    for i in range(2, n + 1):
        for j in range(3, -1, -1):
            dp[j] += dp[j + 1]
    return sum(dp)


if __name__ == '__main__':
    case = 4
    assert count_vowel_strings(case) == 70
