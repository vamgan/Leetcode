class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        first_map = {}
        for letter in words[0]:
            if letter in first_map:
                first_map[letter] += 1
            else:
                first_map[letter] = 1
        for word in words[1:]:
            temp = {}
            for letter in word:
                if letter in first_map:
                    if letter in temp:
                        temp[letter] += 1
                    else:
                        temp[letter] = 1
            for key in first_map:
                if key in temp:
                    first_map[key] = min(first_map[key], temp[key])
                else:
                    first_map[key] = 0
        res = []
        for key, val in first_map.items():
            if val > 0:
                temp = [key] * val
                res.extend(temp)
        return res