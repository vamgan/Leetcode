class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freq = collections.Counter(s)
        count = 0
        for key, val in freq.items():
            if val % 2 != 0:
                count += 1
                if count > 1:
                    return False
        return True