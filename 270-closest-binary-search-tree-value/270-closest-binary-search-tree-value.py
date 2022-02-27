# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def dfs(node):
            if not node:
                return
            if abs(target - node.val) < self.minVal:
                self.minVal = abs(target - node.val)
                self.res = node.val
            if target <= node.val:
                dfs(node.left)
            if target >= node.val:
                dfs(node.right)
        self.minVal = math.inf
        self.res = 0
        dfs(root)
        return self.res