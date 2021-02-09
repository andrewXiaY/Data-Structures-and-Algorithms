"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""


"""
思路：普通的dp，dp[i]代表现在卖出去可能的最高价格
dp[i] = max(dp[i-1], max_j(dp[j-2] + prices[i] - prices[j]))
要考虑dp[i-1]的情况是，我们今天啥也不干的收益是多少
中间max_j(dp[j-2] + prices[i] - prices[j])是假设在j时间点买入股票，i时间点卖出能获得的收益，这样我们遍历每一个可能的j（0 -> i）
其中需要注意的是因为我们有cooldown，所以总体收益是dp[j - 2] + prices[i] - prices[j]这说明j-1那一天我们啥都不能干
"""

# 方法一
def solve(prices):
    n = len(prices)

    dp = [0] * (n+2)  # 为了方便逻辑

    for i in range(2, n + 2):
        for j in range(2, i):
            dp[i] = max(dp[i-1], dp[j-2] + prices[i-2] - prices[j - 2], dp[i])

    return max(dp)


# 方法二 （平行计算）
if __name__ == '__main__':
    assert solve([1, 2, 3, 0, 2]) == 3
