class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        wordSorted = sorted(words, key=lambda word: [order.index(i) for i in word])
        return words == wordSorted