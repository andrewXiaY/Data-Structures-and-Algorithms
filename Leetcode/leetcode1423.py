"""
There are several cards arranged in a row, and each card has an associated number of points The points are given in the
integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
"""


"""
思路：因为我们从两边选数，那么我们可以通过维护一个 n-k 长度的window，然后从左往右移动，然后使用全部数的和减去这个window sum，然后去这个值的最大值
"""


def solve(cards, k):
    n = len(cards)
    total = sum(cards)
    if k > len(cards):
        return 0
    elif n == k:
        return total

    window_sum = sum(cards[:n-k])
    m = total - window_sum

    for i in range(k):
        window_sum = window_sum - cards[i] + cards[i+n-k]
        m = max(m, total - window_sum)

    return m


if __name__ == '__main__':
    assert solve([1, 2, 3, 4, 5, 6, 1], 3) == 12
    assert solve([1, 79, 80, 1, 1, 1, 200, 1], 3) == 202