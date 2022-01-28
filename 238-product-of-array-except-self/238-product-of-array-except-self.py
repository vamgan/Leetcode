class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]
        for i in range(1,len(nums)):
            answer.append(answer[i-1] * nums[i-1])
        print(answer)
        r = 1
        for i in reversed(range(len(nums))):
            answer[i] = answer[i] * r
            r *= nums[i]
        return answer