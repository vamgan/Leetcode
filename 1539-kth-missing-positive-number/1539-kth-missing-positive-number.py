class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ptr = 0
        count = 0
        i = 0
        for i in range(1,arr[-1]):
            if i == arr[ptr]:
                ptr += 1
            else:
                count += 1
                if count == k:
                    return i
        return i + (k - count) + 1