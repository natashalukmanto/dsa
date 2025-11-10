from typing import List, Optional
from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Optimal
def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    columns_mapping = defaultdict(list)
    queue = deque([(root, 0)])
    min_col = max_col = 0

    while queue:
        node, col = queue.popleft()
        if node:
            columns_mapping[col].append(node.val)
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            queue.append((node.left, col - 1))
            queue.append((node.right, col + 1))

    return [columns_mapping[x] for x in range(min_col, max_col + 1)]


# Cleaned BFS
def verticalOrder00(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    columns_mapping = defaultdict(list)
    queue = deque([(root, 0)])

    def bfs(root):
        while queue:
            node, col = queue.popleft()
            if node:
                columns_mapping[col].append(node.val)
                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))

    bfs(root)

    return [columns_mapping[x] for x in sorted(columns_mapping.keys())]


# First Attempt
def verticalOrder0(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    columns_mapping = defaultdict(list)
    queue = deque([(root, 0)])

    def bfs(root):
        while queue:
            node, col = queue.popleft()
            columns_mapping[col].append(node.val)
            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

    bfs(root)

    columns_mapping = dict(sorted(columns_mapping.items()))
    print(columns_mapping)

    res = []

    for col, items in columns_mapping.items():
        res.append(items)

    return res
