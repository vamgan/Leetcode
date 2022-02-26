class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low , high = max(weights), sum(weights)
        def possible(packages,day):
            s = 0
            for i in weights:
                s += i
                if s > packages:
                    s = i
                    day -= 1
                if day == 0:
                    break
            return day > 0
        while low <= high:
            mid = (low + high) //2
            if possible(mid, days):
                high = mid - 1
            else:
                low = mid + 1
        return low
            
