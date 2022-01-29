class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        i = 0
        while i < len(intervals):
            upper = intervals[i][1]
            j = i + 1
            while j < len(intervals):
                if intervals[j][0] <= upper:
                    if intervals[j][1] > upper:
                        upper = intervals[j][1]
                    intervals.pop(j)
                    j -= 1
                else:
                    break
                j += 1
            intervals[i][1] = upper
            i += 1
        return intervals