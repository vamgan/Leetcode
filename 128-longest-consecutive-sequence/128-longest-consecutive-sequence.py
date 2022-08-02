class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_streak = 0
        for i in nums:
            if i - 1 not in nums_set:
                running_streak = 0
                curr_num = i
                while curr_num in nums_set:
                    curr_num += 1
                    running_streak += 1
                max_streak = max(max_streak, running_streak)
            else:
                continue
        return max_streak