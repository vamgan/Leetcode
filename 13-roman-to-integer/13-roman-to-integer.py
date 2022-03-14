class Solution:
    def romanToInt(self, s: str) -> int:
        mapper = {
            'I': 1,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM':900,
            'V':5,
            'X': 10,
            'L':50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        i = 0
        res = 0
        while i < len(s):
            if s[i:i+2] in mapper:
                res += mapper[s[i:i+2]]
                i += 1
            else:
                res += mapper[s[i]]
            i += 1
        return res