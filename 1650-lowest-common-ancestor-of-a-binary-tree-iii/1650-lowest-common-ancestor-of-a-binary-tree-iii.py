"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        root = p
        self.res = None
        while root.parent:
            root = root.parent
        def helper(node):
            if not node:
                return False
            left = helper(node.left)
            right = helper(node.right)
            
            mid = node == p or node == q
            if left + right + mid > 1:
                self.res = node
            return mid or left or right
        helper(root)
        return self.res