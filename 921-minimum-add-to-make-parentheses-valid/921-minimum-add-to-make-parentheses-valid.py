class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        for i in s:
            if i == '(':
                stack.append("(")
            elif i == ')':
                if stack:
                    stack.pop()
                else:
                    count += 1
        if stack:
            count += len(stack)
        return count