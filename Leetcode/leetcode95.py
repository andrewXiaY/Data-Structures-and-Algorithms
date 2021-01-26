# Unique Binary Search Trees II
# 这个题和96相同，96是计算出数目，95是把所有的特有结构找出来
from DataStructures.Trees import TreeNode, preorder_traversal_iterative


"""
思路：
和96相同，这边把每个数的左子树找出来，右子树找出来，然后将当前数作为根节点，形成一棵树，将所有这样的树
放到一起即是答案
"""


def solve(n):
    def recur_build(left, right):
        if left > right:  # 返回条件
            return [None]
        trees = []

        for i in range(left, right + 1):
            left_subtrees = recur_build(left, i - 1)
            right_subtrees = recur_build(i + 1, right)

            for l in left_subtrees:
                for r in right_subtrees:
                    trees.append(TreeNode(i, l, r))
        return trees

    return recur_build(1, n) if n else []

trees = solve(3)
for t in trees:
    # print(t.data)
    print(preorder_traversal_iterative(t))
