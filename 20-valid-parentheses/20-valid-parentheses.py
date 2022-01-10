class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketdict = {"(": ")", "[": "]",  "{": "}"}
        for i in s:
            if i in bracketdict:
                stack.append(i)
            elif stack and i == bracketdict[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []