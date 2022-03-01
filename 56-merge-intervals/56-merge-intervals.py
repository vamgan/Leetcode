class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        for i in intervals:
            if res and i[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], i[1])
            else:
                res.append(i)
        return res