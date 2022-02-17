class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        i = 0
        while i < len(s):
            if res and s[i] == res[-1]:
                    res.pop()
            else:
                res.append(s[i])
            i += 1
        return ''.join(res)