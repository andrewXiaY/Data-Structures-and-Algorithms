# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's
# in their binary representation and return them as an array.

"""
通过记录已经计算过的数的二进制位数，
一个数右移一位肯定小于等于现在的数，
因为已经计算过之前的，所以可以通过记录的方式得到
"""


def solve(num):
    dp = [0] * (num + 1)

    for i in range(num + 1):
        dp[i] = dp[i >> 1] + i % 2

    return dp


if __name__ == "__main__":
    assert solve(5) == [0, 1, 1, 2, 1, 2]