# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def levelOrderHelper(node, level, res):
            if not node:
                return
            if len(res) - 1 < level:
                res.append([node.val])
            else:
                res[level].append(node.val)
            levelOrderHelper(node.left, level + 1, res)
            levelOrderHelper(node.right, level + 1, res)
        res = []
        levelOrderHelper(root, 0, res)
        return res