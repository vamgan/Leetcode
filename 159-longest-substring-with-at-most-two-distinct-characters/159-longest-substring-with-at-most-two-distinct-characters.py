class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        idx_map = {}
        left, right = 0, 0
        max_len = 0
        while left <= right and right < len(s):
            idx_map[s[right]] = right
            if len(idx_map) == 3:
                max_len = max(max_len, right - left)
                left = min(idx_map.values())
                del idx_map[s[left]]
                left += 1
            right += 1
        max_len = max(max_len, right - left)
        return max_len
                
                