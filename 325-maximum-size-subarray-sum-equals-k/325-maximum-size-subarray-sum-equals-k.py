class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        mapper = {}
        running_sum = 0
        max_length = 0
        for i,n in enumerate(nums):
            running_sum += n
            if running_sum == k:
                max_length = i + 1
            if running_sum - k in mapper:
                max_length = max(max_length, i - mapper[running_sum - k])
            if running_sum not in mapper:
                mapper[running_sum] = i
        return max_length
            