class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        numsA, numsB = nums1, nums2
        if len(numsA) > len(numsB):
            numsA, numsB = numsB, numsA
        total = len(numsA) + len(numsB)
        totalMid = total // 2
        leftA = 0
        rightA = len(numsA) - 1
        while True:
            midA = (rightA + leftA) // 2
            midB = totalMid - midA - 2
            
            left_A = numsA[midA] if midA >= 0 else float('-inf')
            right_A = numsA[midA + 1] if midA + 1 < len(numsA) else float('inf')
            left_B = numsB[midB] if midB >= 0 else float('-inf')
            right_B = numsB[midB + 1] if midB + 1 < len(numsB) else float('inf')
            if left_A <= right_B and left_B <= right_A:
                if total % 2 == 0:
                    return (max(left_A, left_B) + min(right_A, right_B)) / 2
                return min(right_A, right_B)
            elif left_A > right_B:
                rightA = midA - 1
            else:
                leftA  = midA + 1