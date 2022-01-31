class Solution(object):
    def minFlipsMonoIncr(self, s: str) -> int:
            count1s, count0s, best = 0, 0, len(s)
            for char in s:
                if char == "1":
                    count1s += 1
            for char in reversed(s):
                best = min(best, count1s+count0s) 
                if char == "0":
                    count0s += 1
                else:
                    count1s -= 1
            return min(best, count1s+count0s) 