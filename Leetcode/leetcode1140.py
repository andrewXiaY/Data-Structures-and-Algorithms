"""
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile
has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.
Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.
"""

def solve(piles):

    N = len(piles)
    dp = {}

    # 通过深度优先得到以start开始，可取m个开始
    def dfs(start, m):

        # 如果start这个点大于piles的总长度
        # base case
        if start >= N:
            return 0

        # 如果可以拿走剩下的
        if N - start < m:
            return sum(piles[start:])
        # 如果这个已经计算过
        if (start, m) in dp:
            return dp[(start, m)]

        score = 0
        total_score = sum(piles[start:])
        # 考虑拿走前x个，那么对手就会拿走dfs（start + x，max（x， m））个
        # 剩下的分数就是总分减去对手得分
        for x in range(1, 2*m + 1):
            op_score = dfs(start+x, max(x, m))
            score = max(score, total_score - op_score)

        dp[(start, m)] = score

        return score
    return dfs(0, 1)


if __name__ == '__main__':
    assert solve([1,2,3,4,5,100]) == 104
