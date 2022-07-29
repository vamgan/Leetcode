class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total_sum = 0
        n = len(arr)
        for i, x in enumerate(arr):
            left = i + 1
            right = n - i
            total_sum += (((left * right) + 1) //2) * x
        return total_sum