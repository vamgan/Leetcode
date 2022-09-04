class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        dic = {}
        left, right = 0, 0
        max_len = 0
        while left <= right and right < len(s):
            dic[s[right]] = right
            if len(dic) == 3:
                max_len = max(max_len, right - left)
                left = min(dic.values())
                del dic[s[left]]
                left += 1
            right += 1
        max_len = max(max_len, right - left)
        return max_len
                
                