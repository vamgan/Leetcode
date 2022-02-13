# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(root, low, high):
            if not root:
                return
            if root.val >= low and root.val <= high:
                self.answer += root.val
            if root.val >= low:
                helper(root.left, low, high)
            if root.val <= high:
                helper(root.right, low, high)
        self.answer = 0
        helper(root,low,high)
        return self.answer