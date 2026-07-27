import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# dfs sol
def minDepthDFS(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    if not root.left:
        return 1 + self.minDepthDFS(root.right)
    elif not root.right:
        return 1 + self.minDepthDFS(root.left)

    return 1 + min(self.minDepthDFS(root.left), self.minDepthDFS(root.right))


# bfs sol
def minDepthBFS(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    q = collections.deque([root])
    depth = 1

    while q:
        q_size = len(q)

        for _ in range(q_size):
            node = q.popleft()

            if not node:
                continue

            if not node.left and not node.right:
                return depth

            q.append(node.left)
            q.append(node.right)

        depth += 1

    return -1
