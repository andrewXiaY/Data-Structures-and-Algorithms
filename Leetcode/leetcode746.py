# Min cost climbing stairs

# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
# Once you pay the cost, you can either climb one or two steps. You need to find minimum
# cost to reach the top of the floor, and you can either start from the step with index 0,
# or the step with index 1.

# terate backwards, current cost = cost[i] + min(prev_cost1, prev_cost2)
# prev_cost1 is the cost if we start from i + 2 to the end
# prev_cost2 is the cost if we start from i + 1 to the end
def solve(cost):
    size = len(cost)

    prev1, prev2 = 0, 0

    for i in range(size - 1, -1, -1):
        cur = cost[i] + min(prev1, prev2)
        prev1 = prev2
        prev2 = cur

    return min(prev1, prev2)


if __name__ == "__main__":
    costs = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

    print(solve(costs))