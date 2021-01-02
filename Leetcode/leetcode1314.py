# matrix block sum
# Use the concept of range sum to solve this problem

# Given a m * n matrix mat and an integer K, return a matrix answer where each answer[i][j] is the sum of all elements
# mat[r][c] for i - K <= r <= i + K, j - K <= c <= j + K, and (r, c) is a valid position in the matrix.
#
# Example 1:
#
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
# Output: [[12,21,16],[27,45,33],[24,39,28]]
# Example 2:
#
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
# Output: [[45,45,45],[45,45,45],[45,45,45]]


def solve(mat, k):
    m, n = len(mat), len(mat[0])
    range_sum = [[0] * (n + 2) for _ in range(m + 2)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            range_sum[i][j] = range_sum[i-1][j] + range_sum[i][j-1] - range_sum[i-1][j-1] + mat[i-1][j-1]

    ans = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            lx, ux, ly, uy = max(0, i - k), min(m, i + k + 1), max(0, j - k), min(n, j + k + 1)
            ans[i][j] = range_sum[ux][uy] - range_sum[ux][ly] - range_sum[lx][uy] + range_sum[lx][ly]
    return ans


if __name__ == '__main__':
    case = [[1,2,3],[4,5,6],[7,8,9]]
    print(solve(case, 1))
    assert solve(case, 1) == [[12,21,16],[27,45,33],[24,39,28]]
