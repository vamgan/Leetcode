class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        runningIdx = 0
        i = 0
        num = ''
        while i < len(abbr):
            if abbr[i].isdigit():
                num += abbr[i]
            else:
                if num:
                    if num[0] == '0':
                        return False
                    runningIdx += int(num)
                    num = ''
                if runningIdx >= len(word) or word[runningIdx] != abbr[i]:
                    return False
                runningIdx += 1
                
            i += 1
        if num and num[0] != '0':
            runningIdx += int(num)
        if runningIdx == len(word):
            return True
        return False
        