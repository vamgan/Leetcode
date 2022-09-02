# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [(root,0)]
        res = []
        prev_level = 0
        temp_sum = 0
        temp_count = 0
        while queue:
            node, level = queue.pop(0)
            if level != prev_level:
                res.append(temp_sum / temp_count)
                temp_sum = node.val
                temp_count = 0
            else:
                temp_sum += node.val
            temp_count += 1
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
            prev_level = level
        res.append(temp_sum / temp_count)
        return res