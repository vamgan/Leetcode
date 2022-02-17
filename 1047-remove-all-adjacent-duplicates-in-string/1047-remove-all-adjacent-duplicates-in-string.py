class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        i = 0
        while i < len(s):
            if res:
                if s[i] != res[-1]:
                    res.append(s[i])
                else:
                    res.pop()
            else:
                res.append(s[i])
            i += 1
        print(res)
        return ''.join(res)