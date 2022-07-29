class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = 0
        for i in data:
            if i == 1:
                ones += 1
        left = 0
        right = 0
        countzeroes = 0
        minswaps = len(data)
        if ones == 1 or ones == 0:
            return 0
        while left <= right and right < len(data):
            if data[right] == 0:
                countzeroes += 1
            if right - left + 1 == ones:
                minswaps = min(minswaps, countzeroes)
                if data[left] == 0:
                    countzeroes -= 1
                left += 1
            right += 1
        return minswaps