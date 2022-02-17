class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        mapper = [[key,value] for key,value in freq.items()]
        mapper.sort(key = lambda x:x[1], reverse = True)
        return [mapper[i][0] for i in range(k)]
    