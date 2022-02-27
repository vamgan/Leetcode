class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        invalid = 0
        def isValid(s):
            i = 0
            j = len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        while left < right:
            if s[left] != s[right]:
                left = isValid(s[:left] + s[left + 1:])
                if left:
                    return True
                right = isValid(s[:right] + s[right + 1:])
                if right:
                    return True
                return False
            left += 1
            right -= 1
        return True
        
        
        