class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opening = 0
        count = 0
        for i in s:
            if i == '(':
                opening += 1
            elif i == ')':
                if opening <= 0:
                    count += 1
                else:
                    opening -= 1
        return opening + count