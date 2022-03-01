class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opening = 0
        count = 0
        for i in s:
            if i == "(":
                opening += 1
            elif i == ")":
                if opening:
                    opening -=1
                else:
                    count += 1
        return opening + count