# Lowest Common Ancestor of a Binary Tree

ans = None

def solve(root, p, q):
    def recur_tree(current_node):
        if not current_node:
            return False

        left = recur_tree(current_node.left)
        right = recur_tree(current_node.right)

        mid = current_node == p or current_node == q

        if left + right + mid >= 2:
            ans = current_node

        return left or right or mid

    recur_tree(root)
