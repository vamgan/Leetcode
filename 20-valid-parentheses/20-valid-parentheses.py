class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = {'(':')', '{':'}', '[':']'}
        for i in s:
            if i in opening:
                stack.append(i)
            else:
                if not stack or opening[stack.pop()] != i:
                   return False
        if not stack:
            return True
        return False
                