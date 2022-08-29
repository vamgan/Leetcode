class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs[1:]:
            temp = ""
            for l in range(len(prefix)):
                if l < len(word) and word[l] == prefix[l]:
                    temp += word[l]
                else:
                    break
            prefix = temp
        return prefix