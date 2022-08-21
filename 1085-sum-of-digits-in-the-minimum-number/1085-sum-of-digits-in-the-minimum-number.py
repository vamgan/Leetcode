class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        min_num = min(nums)
        sp = [i for i in str(min_num)]
        sp = '+'.join(sp)
        if eval(sp) % 2 == 0:
            return 1
        return 0
        