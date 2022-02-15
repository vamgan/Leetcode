from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        elif k == 1:
            return True

        cumulative_sum = 0
        seen_sum_idx = {0: -1}

        for i, e in enumerate(nums):
            cumulative_sum = (cumulative_sum + e) % k
            idx = seen_sum_idx.setdefault(cumulative_sum, i)
            if i - idx >= 2:
                return True
        
        return False
            