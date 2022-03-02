class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxS = nums[0]
        runningS = nums[0]
        for i in nums[1:]:
            runningS = max(runningS + i, i)
            maxS = max(maxS,runningS)
        return maxS