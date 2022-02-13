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
        self.ans = None
        node = p
        while node:
            if node.parent:
                node = node.parent
            else:
                break
        
        def dfs(node):
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            
            mid = node == p or node == q
            if mid + left + right >=2:
                self.ans = node
            return mid or left or right
        dfs(node)
        return self.ans