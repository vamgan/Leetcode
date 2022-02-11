# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None or (root.right is None and root.left is None):
            return root
        arr = []
        def helper(root, arr):
            if not root:
                return
            else:
                arr.append(root.val)

            helper(root.left, arr)
            helper(root.right, arr)
        
        helper(root, arr)
        print(arr)
        for i in range(len(arr) - 1):
            root.val = arr[i]
            root.right = TreeNode()
            root.left =  None
            root = root.right
        root.val = arr[-1]
        
            
        