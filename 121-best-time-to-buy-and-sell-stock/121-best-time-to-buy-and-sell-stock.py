class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = prices[0]
        maxP = 0
        for i in prices:
            maxP = max(maxP, i - minP)
            minP = min(minP, i)
        return maxP