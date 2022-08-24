class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        dic = [""] * numRows
        idx = 0
        direction = 1
        for letter in s:
            dic[idx] += letter
            if idx == numRows - 1:
                direction = -1
            elif idx == 0:
                direction = 1
            idx += direction
        return "".join(dic)