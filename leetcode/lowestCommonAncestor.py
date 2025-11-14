# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

def lowestCommonAncestor(p: 'Node', q: 'Node') -> 'Node':
    def get_depth(node):
        depth = 0
        while node:
            depth += 1
            node = node.parent
        return depth
    
    depth_p, depth_q = get_depth(p), get_depth(q)

    if depth_p < depth_q:  # p is always the deeper node
        p, q = q, p        # this is because we want to start at the same level going up

    depth_diff = abs(depth_p - depth_q)
    while depth_diff:
        depth_diff -= 1
        p = p.parent
    
    while p is not q:
        p, q = p.parent, q.parent
    
    return p

def lowestCommonAncestor(p: 'Node', q: 'Node') -> 'Node':
    parent_p, parent_q = p, q

    while parent_p is not parent_q:
        parent_p = q if parent_p is None else parent_p.parent
        parent_q = p if parent_q is None else parent_q.parent
    
    return parent_p
