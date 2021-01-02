from DataStructures.Trees import BST
"""
Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Here is the example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

# 思路：将每层的最右边的那个node找出来，我们可以通过维护一个queue，在这个queue中保存下一层所有的node以及其对应的层数，顺序是从右至左，这样就能找出
# 所有的最右边的node，同时维护一个result的dictionary，每层最右边的node保存在result中，这样某一层如果有结果在result中则不需要更新


def solve(root):
    # root为空则返回空的list
    if not root:
        return []

    queue = [(root, 0)]
    result = {}

    while queue:
        cur_node, cur_level = queue.pop(0)

        if cur_level not in result:
            result[cur_level] = cur_node.data

        if cur_node.right:
            queue.append((cur_node.right, cur_level + 1))

        if cur_node.left:
            queue.append((cur_node.left, cur_level + 1))

    return [v for k, v in result.items()]


if __name__ == "__main__":
    # 这里使用了我自己写的bst，但是不一定限于bst
    bst = BST()

    bst.add(1)
    bst.add(0)
    bst.add(7)
    bst.add(-9)

    print(solve(bst.root))  # 结果应该是 [1, 7, 9]
