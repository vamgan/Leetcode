class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return list(nums)[-k]