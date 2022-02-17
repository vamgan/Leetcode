class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        idx = 0
        wordIdx = 0
        s = ''
        num = ''
        while idx < len(abbr):
            if abbr[idx].isdigit():
                num += abbr[idx]
            else:
                if num != '':
                    if num[0] == '0' or wordIdx + int(num) > len(word):
                        print('f')
                        return False
                    s += word[wordIdx: wordIdx + int(num)]
                    wordIdx += int(num)
                s += abbr[idx]
                num = ''
                wordIdx += 1
            idx += 1
        print(s)
        if num != '':
                    if num[0] == '0' or wordIdx + int(num) > len(word):
                        print('f')
                        return False
                    s += word[wordIdx: wordIdx + int(num)]
        return s == word
            
            
            
                
                
                