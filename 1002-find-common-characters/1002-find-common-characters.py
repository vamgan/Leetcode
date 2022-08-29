class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        final = {}
        for letter in words[0]:
            if letter in final:
                final[letter] += 1
            else:
                final[letter] = 1
        for word in words[1:]:
            temp = {}
            for letter in word:
                if letter in temp:
                    temp[letter] += 1
                else:
                    temp[letter] = 1
            for key in final:
                if key in temp:
                    final[key] = min(final[key], temp[key])
                else:
                    final[key] = 0
        print(final)
        res = []
        for key, val in final.items():
            if val > 0:
                temp = [key] * val
                res.extend(temp)
        return res