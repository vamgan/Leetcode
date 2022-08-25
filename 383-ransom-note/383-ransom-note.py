class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for letter in magazine:
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1
        for letter in ransomNote:
            if letter not in dic or dic[letter] == 0:
                return False
            dic[letter] -= 1
        return True