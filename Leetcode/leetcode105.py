#  Construct Binary Tree from Preorder and Inorder Traversal
# 在shopee的OA中遇到过
from DataStructures.Trees import TreeNode, inorder_traversal_iterative, preorder_traversal_iterative, \
    postorder_traversal_iterative

"""
思路：preorder中的第一个element是root，这个element将inorder list分成左子树和右子树，这样我们可以通过递归的方式构建左子树和右子树
"""


def solve(preorder, inorder):
    def recur_build(left, right, val_idx):
        if left == right:
            return None
        else:
            c_val = preorder.pop(0)
            ind = val_idx[c_val]
            root = TreeNode(c_val)
            root.left = recur_build(left, ind, val_idx)
            root.right = recur_build(ind+1, right, val_idx)

            return root

    v_id = {val: idx for idx, val in enumerate(inorder)}

    return recur_build(0, len(inorder), v_id)


if __name__ == "__main__":
    tree = solve([3,9,20,15,7], [9,3,15,20,7])
    print(inorder_traversal_iterative(tree))
    print(postorder_traversal_iterative(tree))
    print(preorder_traversal_iterative(tree))