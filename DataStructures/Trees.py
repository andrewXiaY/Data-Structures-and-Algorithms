# This is the class of several tree data structures
# Reference: https://blog.csdn.net/sgbfblog/article/details/7773103
# Reference: https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/


# We could also store key and value in each node
class TreeNode:

    def __init__(self, data=None, left=None, right=None, parent=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.data = data


# This is a simple unbalanced tree, so the worst search time could be O(n)
class BST:

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def _insert(self, value, current_node):
        if current_node.data > value and current_node.left:
            self._insert(value, current_node.left)
        elif current_node.data > value and not current_node.left:
            current_node.left = TreeNode(value, parent=current_node)
        elif current_node.data < value and current_node.right:
            self._insert(value, current_node.right)
        elif current_node.data < value and not current_node.right:
            current_node.right = TreeNode(value, parent=current_node)

    def add(self, value):
        if not self.root:
            self.root = TreeNode(data=value)
        else:
            self._insert(value, self.root)
        self.size += 1

    def search(self, value):
        if not self.root:
            return False

        c_node = self.root
        while c_node:
            if c_node.data == value:
                return True
            elif c_node.data > value:
                c_node = c_node.left
            else:
                c_node = c_node.right

        return False


# inorder traversal: left -> root -> right
def inorder_traversal_recursive(root: TreeNode, order: [int]):
    if root:
        inorder_traversal_recursive(root.left, order)
        order.append(root.data)
        inorder_traversal_recursive(root.right, order)


def inorder_traversal_iterative(root: TreeNode) -> [int]:
    result, stack = [], []
    c_node = root
    while stack or c_node:
        if c_node:  # put all left nodes in stack, the node with larger depth will be in the most front of the stack
            stack.append(c_node)
            c_node = c_node.left
        else:
            # once we meet a empty left node, then we pop the node of the most front of the stack
            # which should be the parent of current node
            c_node = stack.pop(-1)
            result.append(c_node.data)
            c_node = c_node.right
    return result


# preorder traversal: root -> left -> right
def preorder_traversal_recursive(root: TreeNode, order: [int]):
    if root:
        order.append(root.data)
        preorder_traversal_recursive(root.left, order)
        preorder_traversal_recursive(root.right, order)


def preorder_traversal_iterative(root: TreeNode):
    stack, result = [root], []
    while stack:
        c_node = stack.pop(-1)
        result.append(c_node.data)
        if c_node.right:
            stack.append(c_node.right)
        if c_node.left:
            stack.append(c_node.left)
    return result


def preorder_traversal_iterative_2(root: TreeNode):
    stack, result = [], []
    c_node = root
    while stack or c_node:
        if c_node:
            result.append(c_node.data)
            stack.append(c_node)
            c_node = c_node.left
        else:
            c_node = stack.pop(-1)
            c_node = c_node.right


# postorder traversal: left -> right -> root
def postorder_traversal_recursive(root: TreeNode, order: [int]):
    if root:
        postorder_traversal_recursive(root.left, order)
        postorder_traversal_recursive(root.right, order)
        order.append(root.data)


def postorder_traversal_iterative(root: TreeNode):
    stack, result = [root], []
    while stack:
        c_node = stack.pop(-1)
        result.append(c_node.data)
        if c_node.left:
            stack.append(c_node.left)
        if c_node.right:
            stack.append(c_node.right)
    return list(reversed(result))


if __name__ == "__main__":
    bst = BST()

    bst.add(10)
    bst.add(3)
    bst.add(7)
    bst.add(8)
    bst.add(15)
    bst.add(20)

    inorder_list= []
    preorder_list = []
    postorder_list = []

    inorder_traversal_recursive(bst.root, inorder_list)
    print(inorder_list)
    print(inorder_traversal_iterative(bst.root))

    preorder_traversal_recursive(bst.root, preorder_list)
    print(preorder_list)
    print(preorder_traversal_iterative(bst.root))

    postorder_traversal_recursive(bst.root, postorder_list)
    print(postorder_list)
    print(postorder_traversal_iterative(bst.root))
