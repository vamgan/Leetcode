class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketdict = {"(": ")", "[": "]",  "{": "}"}
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            elif stack and i == bracketdict[stack[-1]]:
                stack.pop()
            else:
                return False
        if stack == []:
            return True