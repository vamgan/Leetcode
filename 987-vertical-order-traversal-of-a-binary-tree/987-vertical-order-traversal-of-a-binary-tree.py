# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node,col, row):
            nonlocal arr, maxcol, mincol
            if not node:
                return
            if col in arr:
                arr[col].append((row, node.val))
            else:
                arr[col] = [(row, node.val)]
            maxcol = max(maxcol, col)
            mincol = min(mincol, col)
            dfs(node.left, col - 1,row + 1)
            dfs(node.right, col + 1, row + 1)
        arr = {}
        res = []
        maxcol,mincol = 0, 0
        dfs(root, 0,0)
        for i in range(mincol, maxcol+1):
            res.append([val for key,val in sorted(arr[i])])
        return res