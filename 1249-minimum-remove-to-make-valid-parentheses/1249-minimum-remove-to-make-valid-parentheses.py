class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        removeidx = set()
        for i,c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    removeidx.add(i)
        if stack:
            removeidx.update(stack)
        answer = ""
        for i,c in enumerate(s):
            if i not in removeidx:
                answer += c
        return answer