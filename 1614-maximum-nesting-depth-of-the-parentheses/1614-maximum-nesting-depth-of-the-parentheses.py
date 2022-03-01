class Solution:
    def maxDepth(self, s: str) -> int:
        opening = 0
        depth = 0
        for i in s:
            if i == '(':
                opening += 1
                depth = max(depth, opening)
            elif i == ')':
                opening -= 1
        return depth