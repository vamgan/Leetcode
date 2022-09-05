"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [(root, 0)]
        while queue:
            node, level = queue.pop(0)
            for child in node.children:
                queue.append((child,level + 1))
            if len(res) > level:
                res[level].append(node.val)
            else:
                res.append([node.val])
        return res