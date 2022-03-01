class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.set = set()
        for i in range(len(nums)):
            if nums[i] != 0:
                self.set.add(i)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        def helper(vec1, vec2):
            s = 0
            for i in vec1:
                if i in vec2:
                    s += self.nums[i] * vec.nums[i]
            return s
        if len(self.set) > len(vec.set):
            return helper(vec.set, self.set)
        else:
            return helper(self.set, vec.set)

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)