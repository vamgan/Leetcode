class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -math.inf
        curr_sum = 0
        for i in nums:
            if i > curr_sum + i:
                curr_sum = i
            else:
                curr_sum += i
            max_sum = max(curr_sum, max_sum)
        return max_sum
            
            