class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        lengthS = len(s)
        lengthT = len(t)
        if lengthS > lengthT:
            return self.isOneEditDistance(t, s)
        if lengthT - lengthS > 1:
            return False
        for i in range(lengthS):
            if s[i] != t[i]:
                if s == t[:i] + t[i+1:]:
                    return True
                elif s[:i] + s[i+1:] == t[:i] + t[i+1:]:
                    return True
                else:
                    return False
        return lengthS + 1 == lengthT
                