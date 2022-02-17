class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapper = {}
        left = 0
        right = 0
        res = 0
        for idx,val in enumerate(s):
            if val in mapper:
                if mapper[val] >= left:
                    left = mapper[val] + 1
                left
                mapper[val] = idx
                
            else:
                mapper[val] = idx
            right += 1
            res = max(res,right - left)
        return res
        