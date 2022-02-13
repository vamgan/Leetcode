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
        left = 0
        right = len(self.prefix_sum)
        while left <= right:
            mid = (left + right) // 2
            if target < self.prefix_sum[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()