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
            # if s[right] in mapper:
            #     del mapper[s[right]]
            mapper[s[right]] = right
            if len(mapper) == k + 1:
                best_key = min(mapper, key=mapper.get)
                left = mapper[best_key] + 1
                del mapper[best_key]
            right += 1
            max_length = max(max_length, right - left)
        return max_length
            