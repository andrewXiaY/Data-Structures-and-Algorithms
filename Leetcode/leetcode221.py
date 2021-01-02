
def maximal_square(matrix: [[str]]):
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    # initialize dp matrix
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    maximum = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if matrix[i - 1][j - 1] == '1':
                dp[i][j] = min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1

            if maximum < dp[i][j]:
                maximum = dp[i][j]
    return maximum * maximum


if __name__ == "__main__":
    matrix = [["1","0","1","0","0"], ["1","0","1","1","1"], ["1","1","1","1","1"], ["1","0","0","1","0"]]
    print(maximal_square(matrix))