from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# This is editorial DFS
def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    def dfs(root):
        res = 0
        if root:
            if root.val >= low and root.val <= high:
                res += root.val
            if low < root.val:
                res += dfs(root.left)
            if root.val < high:
                res += dfs(root.right)
        return res

    return dfs(root)


# Should be DFS not bfs
def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

    def bfs(root):
        res = 0
        if root and root.val >= low and root.val <= high:
            res += root.val
        if root.left:
            res += bfs(root.left)
        if root.right:
            res += bfs(root.right)
        return res

    return bfs(root)


# This is editorial's BFS
def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    res, stack = 0, [root]

    while stack:
        node = stack.pop()
        if node:
            if node.val >= low and node.val <= high:
                res += node.val
            if node.val > low:
                stack.append(node.left)
            if high > node.val:
                stack.append(node.right)

    return res
