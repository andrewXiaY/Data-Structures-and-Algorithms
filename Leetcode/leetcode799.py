"""
We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th
row.  Each glass holds one cup of champagne.

Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid
poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any
excess champagne will fall equally to the left and right of those glasses, and so on.
(A glass at the bottom row has its excess champagne fall on the floor.)

For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured,
the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full
- there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half
full, and the two outside glasses are a quarter full, as pictured below.

Now after pouring some non-negative integer cups of champagne, return how full the jth glass in the ith row is
(both i and j are 0-indexed.)
"""


"""
思路：通过simulation的方式，从顶端开始，有K瓶，每次通过一个地方的时候会有 （K - 1） / 2流到下面两个地方 
"""


def solve(poured, x, y):
    dp = [[0] * i for i in range(1, 102)]

    dp[0][0] = poured

    for i in range(x+1):
        for j in range(i+1):
            q = (dp[i][j] - 1) / 2
            if q > 0:
                dp[i+1][j] += q
                dp[i+1][j+1] += q

    return min(1, dp[x][y])


if __name__ == '__main__':
    assert solve(2, 1, 1) == 0.5
    assert solve(10000009, 33, 17) == 1.0

