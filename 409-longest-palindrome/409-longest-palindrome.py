
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = collections.Counter(s)
        ans = 0
        for key in count:
            if ans % 2 == 0:
                ans += count[key]
            else:
                ans += count[key]//2 * 2
        return ans