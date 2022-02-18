class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        for i in prices:
            if i < minPrice:
                minPrice = i
            if i - minPrice > maxProfit:
                maxProfit =  i - minPrice
        return maxProfit