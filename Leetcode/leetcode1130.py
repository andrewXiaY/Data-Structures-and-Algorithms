# Given an array arr of positive integers, consider all binary trees such that:
#
# Each node has either 0 or 2 children;
# The values of arr correspond to the values of each leaf in an in-order traversal of the tree.  (Recall that a node is
# a leaf if and only if it has 0 children.)
# The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree
# respectively.
# Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.
# It is guaranteed this sum fits into a 32-bit integer.

"""
注意到三个数从左到右是高中低的模式那么就能得到最小值。使用stack，不断将数压入stack中，如果当前数大于stack[-1]，说明打破了高中低的模式，
那么需要判断当前数于stack[-2]的关系 （模式为高低中，判断 高*低 和 中*高，得到最小值），然后pop stack，并将当前值压入stack中
"""


def solve(nums):
    stack = [float('inf')]

    ans = 0
    for c in nums:
        while c >= stack[-1]:
            l = stack.pop()
            ans += l * min(c, stack[-1])
        stack.append(c)

    while len(stack) > 2:
        ans += stack.pop() * stack[-1]

    return ans


if __name__ == '__main__':
    assert solve([6, 2, 4]) == 32
    assert solve([10, 6, 5, 3, 9]) == 189
