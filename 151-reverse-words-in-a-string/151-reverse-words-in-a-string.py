class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        newString = ""
        finalString = ""
        for i in range(len(s) - 1,-1,-1):
            if s[i] == " ":
                if newString.isalnum():
                    print(newString)
                    finalString += newString + " "
                    newString = ""
            else:
                newString = s[i] + newString
        
        return finalString + newString