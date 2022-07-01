class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arraySum = sum(nums)
        runningSum = 0
        for i,n in enumerate(nums):
            if runningSum * 2 == arraySum - n:
                return i
            runningSum += n
        return -1