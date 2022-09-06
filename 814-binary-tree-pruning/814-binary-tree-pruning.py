# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return
            if not dfs(node.left):
                node.left = None
            if not dfs(node.right):
                node.right = None
                
            if node.val == 1 or node.right or node.left:
                return True
            return False
        if dfs(root):
            return root
        else:
            return None