class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        i = 0
        j = 2
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = check(s, i, i)
            len2 = check(s,i, i+1)
            maxLen = max(len1,len2)
            if maxLen > end - start:
                start = i - (maxLen - 1) // 2
                end = i + maxLen // 2
        return s[start:end+1]
        
    