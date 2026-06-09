# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def goodNodes(root: TreeNode) -> int:

    def dfs(root, current_max):
        if not root:
            return 0

        good_node = 0
        if root.val >= current_max:
            good_node += 1
            current_max = root.val

        return good_node + dfs(root.left, current_max) + dfs(root.right, current_max)

    return dfs(root, root.val)
