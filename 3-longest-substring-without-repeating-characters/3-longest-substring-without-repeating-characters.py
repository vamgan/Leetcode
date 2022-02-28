class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapper = {}
        maxLen = 0
        i = 0
        j = 0
        while j < len(s):
            if s[j] in mapper:
                if i <= mapper[s[j]]:
                    i = mapper[s[j]] + 1
            mapper[s[j]] = j
            maxLen = max(maxLen, j - i + 1)
            j += 1
        return maxLen