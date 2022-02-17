class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wordIdx = 0
        
        num = ''
        for idx,i in enumerate(abbr):
            if i.isdigit():
                if not num and i == '0':
                    return False
                num += i
                continue
            if num != '':
                wordIdx += int(num)
                num = ''
            if wordIdx >= len(word) or i != word[wordIdx]:
                return False
            wordIdx += 1
            
        if num:
            wordIdx += int(num)
        if wordIdx != len(word):
            return False
        return True
                    
                
                
                