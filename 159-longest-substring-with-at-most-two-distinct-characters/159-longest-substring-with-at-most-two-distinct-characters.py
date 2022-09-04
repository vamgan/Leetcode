class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        dic = {}
        left, right = 0, 0
        max_len = 0
        while left <= right and right < len(s):
            dic[s[right]] = right
            if len(dic) == 3:
                max_len = max(max_len, right - left)
                temp_left = right
                for key in dic:
                    temp_left = min(dic[key], temp_left)
                del dic[s[temp_left]]
                left = temp_left + 1
            right += 1
        max_len = max(max_len, right - left)
        return max_len
                
                