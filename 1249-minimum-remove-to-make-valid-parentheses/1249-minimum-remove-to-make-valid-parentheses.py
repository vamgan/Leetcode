class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        invalid = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    invalid.append(i)
        stack.extend(invalid)
        invalid = set(stack)
        newS = ''
        for i in range(len(s)):
            if i not in invalid:
                newS += s[i]
        return newS