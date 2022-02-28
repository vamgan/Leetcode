class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}
        s = 0
        for i, n in enumerate(nums):
            complement = target - n
            if complement in mapper:
                return [mapper[complement], i]
            mapper[n] = i