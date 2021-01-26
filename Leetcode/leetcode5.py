#  Given a string s, return the longest palindromic substring in s.

"""
1. 遍历字符串中的每一个字符
2. 存在两种情况的回文 aba和abba
3. expand_from_center(s, ind, ind)处理aba这种情况，expand_from_center(s, ind, ind + 1)处理abba这种情况
"""

def solve(s):

    def expand_from_center(s_, left, right):
        while left >= 0 and right < len(s_) and s_[left] == s_[right]:
            left -= 1
            right += 1

        return right - left - 1  # 因为最后left和right都多加了一个1，实际上是 right - left + 1 - 2

    if s == '':
        return s
    start = end = 0
    for ind, c in enumerate(s):
        length1 = expand_from_center(s, ind, ind)
        length2 = expand_from_center(s, ind, ind + 1)

        if max(length1, length2) > end - start:
            start = ind - (max(length1, length2) - 1) // 2
            end = ind + max(length1, length2) // 2

    return s[start:end+1]