# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        depth = 0
        answer = []
        if root is None:
            return answer
        def helper(root, depth):
            if depth == len(answer):
                answer.append([root.val])
            else:
                answer[depth].append(root.val)
            if root.left:
                helper(root.left, depth + 1)
            if root.right:
                helper(root.right, depth + 1)
        helper(root, depth)
        return answer
        