# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node,col, row):
            nonlocal arr
            if not node:
                return
            arr.append([node.val,col, row])
            dfs(node.left, col - 1,row + 1)
            dfs(node.right, col + 1, row + 1)
        arr = []
        res = []
        dfs(root, 0,0)
        arr.sort(key = lambda x: (x[1],x[2], x[0]))
        left_most = abs(arr[0][1])
        for i in arr:
            if i[1] + left_most < len(res):
                res[i[1] + left_most].append(i[0])
            else:
                res.append([i[0]])
        return res