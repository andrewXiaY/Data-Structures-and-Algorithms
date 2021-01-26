# Unique Binary Search Trees

"""
Given n, how many structurally unique BST's (binary search trees)
that store values 1 ... n?
"""

"""
思路：动态规划
首先明确一点，将1到n排序好以后，以不同的数i为根节点，i左边的数形成左子树，i右边的数形成右子树
这样构建成的tree在结构上都是不同的，现在的问题就是，左子树有多少种可能的独特结构，右子树有多少种独特的结构
设 C(n) 代表长度为n的序列存在的独特BST个数
F(i, n) 代表长度为n的序列，且以i为root的BST的个数（1 <= i <= n）
那么 C(n) = \sum_{i=1->i=n} F(i, n)

*** 最关键的就是要理解两个点：
1。 sorted的序列中，从左至右将每个数当成根节点，左边的数当左子树，右边的数当右子树这样就能计算出所有的独特结构
2。 长度相同的序列独特结构的BST的数目是相同的
"""

def solve(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        for j in range(1, i + 1):
            dp[i] += dp[j - 1] * dp[i - j]

    return dp[n]

print(solve(3))