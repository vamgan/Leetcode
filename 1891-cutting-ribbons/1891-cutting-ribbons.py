class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def possible(rlen):
            total = 0
            for i in ribbons:
                total += i // rlen
            return total < k
        low, high = 1, max(ribbons)
        if k > sum(ribbons):
            return 0

        while low <= high:
            mid = (low + high) // 2
            if possible(mid):
                high = mid - 1
            else:
                low = mid + 1
        return high
        
                