# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res_sum = root.val
        
        def dfs(node, running_sum):
            nonlocal res_sum
            if not node:
                return 0
            
            running_sum_left = max(0, dfs(node.left, running_sum))
            running_sum_right = max(0, dfs(node.right, running_sum))
            running_sum = max(running_sum_left + node.val, running_sum_right + node.val)
            res_sum = max(res_sum, running_sum_left + running_sum_right + node.val)
            return running_sum
        dfs(root, 0)
        return res_sum