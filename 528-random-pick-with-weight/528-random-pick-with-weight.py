class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.prefix_sum = []
        prefix_sum = 0
        for i in w:
            prefix_sum += i
            self.prefix_sum.append(prefix_sum)
        self.total_sum = prefix_sum
    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        for i, prefix in enumerate(self.prefix_sum):
            if target < prefix:
                return i
    


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()