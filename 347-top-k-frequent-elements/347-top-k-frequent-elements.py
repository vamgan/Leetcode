class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        freq = collections.Counter(nums)
        for key,value in freq.items():
            bucket[value].append(key)
        result = [item for i in bucket for item in i]
        return result[::-1][:k]
    