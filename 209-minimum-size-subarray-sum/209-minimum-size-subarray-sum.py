class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = math.inf
        left = 0
        right = 0
        running_sum = nums[left]
        while left <= right and right < len(nums):
            if running_sum < target:
                right += 1
                if right < len(nums):
                    running_sum += nums[right]
            else:
                min_length = min(min_length, right - left + 1)
                running_sum -= nums[left]
                left += 1
        
        return 0 if min_length == math.inf else min_length
            