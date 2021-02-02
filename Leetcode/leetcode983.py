"""
In a country popular for train travel, you have planned some train travelling one year in advance.
The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2,
then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.
"""

"""
思路1: 考虑全年365天
dp[i] = min(dp[i + 1] + costs[0], dp[i+7] + costs[1], dp[i+30] + costs[2])
通过递归的方式得到结果，base case是当i > 365时返回0，当i在days这个list中是计算上面这个式子，其他时候都计算dp[i+1]
"""

from functools import lru_cache


def solve_day_variant(days, costs):
    daysets = set(days)

    @lru_cache(maxsize=None)
    def dp(d):
        if d > 365:
            return 0
        elif d in daysets:
            return min(dp(d + 1) + costs[0], dp(d + 7) + costs[1], dp(d + 30) + costs[2])
        else:
            return dp(d + 1)

    return dp(1)


"""
思路2：只考虑days里的时间

dp[i] = min(dp[j1] + costs[0], dp[j7] + costs[1], dp[j30] + costs[2])

"""


def solve_window_variant(days, costs):
    n = len(days)

    @lru_cache(maxsize=None)
    def dp(i):
        if i >= n:
            return 0
        ans = float('inf')
        j = i
        for c, d in zip(costs, [1, 7, 30]):
            while j < n and days[j] < days[i] + d:
                j += 1
            ans = min(ans, dp(j) + c)
        return ans

    return dp(0)

