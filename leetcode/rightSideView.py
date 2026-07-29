from typing import List, Optional
from collections import deque
from TreeNode import TreeNode


def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    queue = deque([root])
    res = []

    while queue:
        q_size = len(queue)

        res.append(queue[-1].val)

        for _ in range(q_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return res
