"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you

would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be

[1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer
in the range [30, 100].

"""

"""
hint：
1。从后往前计算
2。假设现在是第i天，气温是t_i，那么对于i之后的日子j，如果气温t_j < t_i, 那么这个温度对于i之前的日子是不会有任何影响的，
因为对于q而言 （q < i）任何比t_i温度低的日子都会被第i天阻拦（也就是第一个高于t_q的温度不可能是i之后小于t_i的温度），
在i之前任何比t_i温度要高的日子都不会被t_i阻拦，同样也不会被任何小于t_i的t_j阻拦（也就是这种情况下第一个高于t_q的温度不可能是i之后小于t_i的温度），
因此我们只需要从后往前遍历，然后保存比当前温度要高的温度
"""


def solve(temperatures):
    n = len(temperatures)
    ans = [0] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and temperatures[i] >= temperatures[stack[-1]]:
            stack.pop()

        if stack:
            ans[i] = stack[-1] - i
        stack.append(i)

    return ans


if __name__ == "__main__":
    assert solve([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
