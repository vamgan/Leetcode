from collections import OrderedDict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0 or s == "":
            return 0
        left = 0
        right = 0
        max_length = 1
        mapper = OrderedDict()
        while right < len(s):
            mapper[s[right]] = right
            if len(mapper) == k + 1:
                idx = min(mapper.values())
                del mapper[s[idx]]
                left = idx + 1
            right += 1
            max_length = max(max_length, right - left)
        return max_length
            