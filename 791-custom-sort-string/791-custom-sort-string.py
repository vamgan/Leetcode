class Solution:
    def customSortString(self, order: str, s: str) -> str:
        mapper = collections.Counter(s)
        res = ""
        for i in order:
            res += i * mapper[i]
            mapper[i] = 0
        for i in mapper:
            if mapper[i] > 0:
                res += i * mapper[i]
        return res