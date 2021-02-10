"""
On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves.
The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction,
then one square in an orthogonal direction.

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go
off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability
that the knight remains on the board after it has stopped moving.
"""

from functools import lru_cache

"""
通过dfs的方式进行
"""
def solve(N, K, r, c):
    @lru_cache(maxsize=None)
    def dfs(x, y, remain_steps):
        nonlocal N
        if x < 0 or y < 0 or x >= N or y >= N:
            return 0

        if remain_steps == 0:
            return 1

        return dfs(x + 2, y + 1, remain_steps - 1) + \
               dfs(x + 1, y + 2, remain_steps - 1) + \
               dfs(x - 1, y + 2, remain_steps - 1) + \
               dfs(x - 1, y - 2, remain_steps - 1) + \
               dfs(x + 1, y - 2, remain_steps - 1) + \
               dfs(x + 2, y - 1, remain_steps - 1) + \
               dfs(x - 2, y + 1, remain_steps - 1) + \
               dfs(x - 2, y - 1, remain_steps - 1)

    return dfs(r, c, K) / 8 ** K


if __name__ == '__main__':
    assert solve(3, 2, 0, 0) == 0.0625
