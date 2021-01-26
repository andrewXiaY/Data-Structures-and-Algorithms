# Serialize and Deserialize Binary Tree
from DataStructures.Trees import BST, TreeNode, inorder_traversal_iterative
"""
思路：使用dfs将tree转化成字符串，同时通过递归的方式将字符串转化成tree
"""

def serialize_tree(root):
    def recur_serialize(_root, string):
        if _root is None:
            string += "null,"
        else:
            string += f"{_root.data},"
            string = recur_serialize(_root.left, string)
            string = recur_serialize(_root.right, string)
        return string

    return recur_serialize(root, "")


def deserialize_tree(string):
    def recur_deserialize(values):
        c_val = values.pop(0)

        if c_val == "null":
            return None
        else:
            c_node = TreeNode(c_val)
            c_node.left = recur_deserialize(values)
            c_node.right = recur_deserialize(values)
            return c_node

    lst = string.split(",")
    return recur_deserialize(lst)


if __name__ == "__main__":
    bst = BST()
    bst.add(10)
    bst.add(2)
    bst.add(7)
    bst.add(-1)
    bst.add(18)
    bst.add(12)

    print(serialize_tree(bst.root))
    print(inorder_traversal_iterative(deserialize_tree(serialize_tree(bst.root))))
