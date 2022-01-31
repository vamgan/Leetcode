class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def helper(s, wordDict, sentence = "", answer = []):
            if s == "":
                answer.append(sentence.strip())
                return
            sent = ""
            for i, c in enumerate(s):
                sent += c
                if sent in wordDict:
                    helper(s[i+1:],wordDict, sentence + sent + " ", answer)
            return answer
        return helper(s,wordDict)