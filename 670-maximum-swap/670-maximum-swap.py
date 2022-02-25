class Solution:
    def maximumSwap(self, num: int) -> int:
        num_ = [int(i) for i in str(num)]
        maxNum = 0
        maxIdx = 0
        recentminIdx = 0
        recentmaxIdx = 0
        for i in range(len(num_) - 1, -1, -1):
            if num_[i] > maxNum:
                maxNum = num_[i]
                maxIdx = i
            elif num_[i] < maxNum:
                recentmaxIdx = maxIdx
                recentminIdx = i

        num_[recentminIdx], num_[recentmaxIdx] = num_[recentmaxIdx], num_[recentminIdx]
        return ''.join([str(i) for i in num_])