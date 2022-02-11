"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        copy = Node(val = node.val, neighbors = [])
        if node.neighbors is []:
            return copy
        visited = {node:copy}
        def helper(node, copy, visited):
            for n in node.neighbors:
                if n in visited:
                    copy.neighbors.append(visited[n])
                    continue
                newN = Node(val = n.val, neighbors = [])
                copy.neighbors.append(newN)
                visited[n] = newN
                helper(n,newN, visited)
            return 
        helper(node, copy, visited)
        return copy