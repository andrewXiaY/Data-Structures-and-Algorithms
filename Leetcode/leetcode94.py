# Binary Tree Inorder traversal 迭代方式
from DataStructures.Trees import  TreeNode

"""
思路：本质上和递归一样，先处理左边的节点，然后中间节点，最后右边节点

任何递归程序都能转换为一个等价的非递归程序，这里我们只需要用一个栈来模拟递归即可

为什么递归都能转化成为一个等价的非递归程序？

因为汇编没有递归，机器码没有递归，那高级语言中的递归如何实现呢？所以必然是可以的
"""
def solve(root):
    stacks = []
    result = []
    cur_node = root

    while cur_node != None or len(stacks):
        # 下面的while循环是寻找以当前node为root的树的最小左子树（从最小左子树开始处理），
        # 并且记录走过的所有节点（这些节点都是处理完左子树之后需要返回的中间节点，以便之后处理右子树）
        while cur_node != None:
            stacks.append(cur_node)
            cur_node = cur_node.left
        cur_node = stacks.pop(-1)

        result.append(cur_node.val)
        # 处理当前node的右子树
        cur_node = cur_node.right

    return result

