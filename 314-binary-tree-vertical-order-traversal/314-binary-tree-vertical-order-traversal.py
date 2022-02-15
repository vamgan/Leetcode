# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        self.arr = []
        def dfs(node, col, row):
            if not node:
                return
            self.arr.append([node.val,col, row])
            dfs(node.left,col - 1, row+1)
            dfs(node.right, col + 1, row+1)
        dfs(root,0,0)
        
        self.arr.sort(key = lambda x: (x[1], x[2]))
        print(self.arr)
        res = [[self.arr[0][0]]]
        for i in range(1,len(self.arr)):
            if self.arr[i-1][1] == self.arr[i][1]:
                res[-1].append(self.arr[i][0])
            else:
                res.append([self.arr[i][0]])
        return res