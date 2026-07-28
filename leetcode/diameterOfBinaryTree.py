from typing import Optional
from TreeNode import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def longest_path(root):
            nonlocal diameter
            if not root:
                return -1

            left, right = longest_path(root.left), longest_path(root.right)

            diameter = max(diameter, left + right + 2)
            return max(left, right) + 1

        longest_path(root)

        return diameter
