class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cum_sum = 0
        mapper = {0:1}
        count = 0
        for i in nums:
            cum_sum += i
            if cum_sum - k in mapper:
                count += mapper[cum_sum - k]
            if cum_sum in mapper:
                mapper[cum_sum] += 1
            else:
                mapper[cum_sum] = 1
        return count
                