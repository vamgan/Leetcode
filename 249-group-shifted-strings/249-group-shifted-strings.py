class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        answer = []
        mapper = {}
        for word in strings:
            diff = ""
            for letter in range(0,len(word) - 1):
                diff += str((ord(word[letter + 1]) - ord(word[letter]) + 26) % 26)
            if len(diff) < len(word):
                diff = "0" + diff
            if diff in mapper:
                mapper[diff].append(word)
            else:
                mapper[diff] = [word]
        print(mapper)
        for array in mapper:
            answer.append(mapper[array])
        return answer