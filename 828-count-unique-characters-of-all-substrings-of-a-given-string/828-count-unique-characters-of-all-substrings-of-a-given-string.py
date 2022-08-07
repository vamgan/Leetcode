class Solution:
    def uniqueLetterString(self, s: str) -> int:
        letter_idx = [[] for _ in range(26)]
        for i in s:
            idx = ord(i) - ord('A')
            letter_idx[idx].append(-1)
        for i, l in enumerate(s):
            idx = ord(l) - ord('A')
            letter_idx[idx].append(i)
        for i in letter_idx:
            if i != []:
                i.append(len(s))
        res = 0
        for i in range(0, len(letter_idx)):
            bucket = letter_idx[i]
            for j in range(1, len(bucket) - 1):
                count = (bucket[j] - bucket[j-1]) * (bucket[j + 1] - bucket[j])
                res += count
        return res