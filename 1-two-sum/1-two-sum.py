class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in mapper:
                return [mapper[diff], idx]
            else:
                mapper[num] = idx
                