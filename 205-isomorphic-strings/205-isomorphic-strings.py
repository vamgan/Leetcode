class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapper = {}
        mapped = set()
        for i,x in enumerate(s):
            if x not in mapper and t[i] not in mapped:
                mapper[x] = t[i]
                mapped.add(t[i])
            else:
                if x not in mapper:
                    return False
                if t[i] != mapper[x]:
                    return False
        return True
                