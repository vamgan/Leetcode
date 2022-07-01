class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runningSum = 0
        res = []
        for i in nums:
            runningSum += i
            res.append(runningSum)
        return res
            