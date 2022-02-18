class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        maxProduct = nums[0]
        minProduct = nums[0]
        for i in nums[1:]:
            temp_max = max(i,  maxProduct * i, minProduct * i)
            minProduct = min(i,  maxProduct * i, minProduct * i)
            maxProduct = temp_max
            result = max(result, maxProduct)
        return result