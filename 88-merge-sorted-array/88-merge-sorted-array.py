class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        answer = []
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                answer.append(nums1[i])
                i += 1
            else:
                answer.append(nums2[j])
                j += 1
        if i < m:
            answer.extend(nums1[i:m])
        else:
            answer.extend(nums2[j:n])
        print(answer)
        for i in range(len(nums1)):
            nums1[i] = answer[i]
        print(nums1)
        return nums1