class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(st):
            i = 0
            j = len(st) - 1
            while i <= j:
                if st[i] != st[j]:
                    return False
                i += 1
                j -= 1
            return True
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                left = check(s[:i] + s[i+1:])
                if left:
                    return True
                if check(s[:j] + s[j+1:]):
                    return True
                return False
            i += 1
            j -= 1
        return True