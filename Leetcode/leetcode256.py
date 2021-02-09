"""
There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.



Example 1:

Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.
Example 2:

Input: costs = []
Output: 0
Example 3:

Input: costs = [[7,6,2]]
Output: 2
"""


"""
思路：从上至下，每一层的最优肯定是上一层的最优加上这一层cost
就像是falling path一样
"""


def solve(costs):
    if len(costs) == 0:
        return 0

    m, n = len(costs), len(costs[0])

    dp = [[0] * n for _ in range(m)]
    dp[0] = costs[0]  # 第一层的cost就是costs里面的第一层

    for i in range(1, m):  # 从第二层开始
        dp[i][0] = min(dp[i - 1][1] + costs[i][0], dp[i - 1][2] + costs[i][0])  # 如果这一层用red，那只能从上一层的green和blue中下来
        dp[i][1] = min(dp[i - 1][0] + costs[i][1], dp[i - 1][2] + costs[i][1])  # 如果这一层用green，那只能从上一层的red和blue中下来
        dp[i][2] = min(dp[i - 1][0] + costs[i][2], dp[i - 1][1] + costs[i][2])  # 如果这一层用blue，那只能从上一层的green和red中下拉

    return min(dp[-1])  # 返回最后一层的最小值


