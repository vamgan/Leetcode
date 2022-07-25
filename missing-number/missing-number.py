class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        array_sum = 0
        for i in range(len(nums) + 1):
            array_sum += i
        for i in nums:
            array_sum -= i
        return array_sum
        
                