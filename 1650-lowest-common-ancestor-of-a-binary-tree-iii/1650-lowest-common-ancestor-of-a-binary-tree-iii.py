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
        a_node = p
        b_node = q
        a_node_set = set()
        while a_node:
            a_node_set.add(a_node.val)
            a_node = a_node.parent
        while b_node:
            if b_node.val in a_node_set:
                return b_node
            b_node = b_node.parent