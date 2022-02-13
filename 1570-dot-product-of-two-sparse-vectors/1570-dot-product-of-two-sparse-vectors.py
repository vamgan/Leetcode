class SparseVector:
    def __init__(self, nums: List[int]):
        self.num = nums
        self.idx = set([idx for idx, i in enumerate(nums) if i])

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        common = self.idx & vec.idx
        product = 0
        for i in common:
            product += self.num[i] * vec.num[i]
        return product
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)