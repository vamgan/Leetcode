class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        change = 0
        for i in range(len(nums) - 1,-1,-1):
            if nums[i] > nums[i - 1]:
                change = i
                break
        if change == 0:
            return nums.reverse()
        ptr1 = change
        ptr2 = len(nums) - 1
        if ptr1 == ptr2:
            nums[change - 1], nums[ptr2] = nums[ptr2], nums[change - 1]
            return nums
        i = change - 1
        j = len(nums) - 1
        while i < j:
            if nums[change-1] < nums[j]:
                nums[change-1], nums[j] = nums[j], nums[change-1]
                break
            j -=1
        while ptr1 < ptr2:
            nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
            ptr1 += 1
            ptr2 -= 1
        return nums
                
            
            