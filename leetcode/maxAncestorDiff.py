from typing import Optional
from TreeNode import TreeNode

def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    min_value = max_value = root.val

    def dfs(root, min_value, max_value):
        if not root:
            return abs(max_value - min_value)

        min_value = min(root.val, min_value)
        max_value = max(root.val, max_value)

        left = dfs(root.left, min_value, max_value)
        right = dfs(root.right, min_value, max_value)

        return max(left, right)

    return dfs(root, min_value, max_value)
