"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to
sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

"""
遍历列表，找到i之前最低价格买入，然后以当前价格卖出，算出利润
"""


def solve(prices):
    lowest_price = prices[0]
    max_profit = 0

    for c in prices:
        lowest_price = min(lowest_price, c)
        max_profit = max(max_profit, c - lowest_price)

    return max_profit
