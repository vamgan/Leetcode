class SparseVector:
    def __init__(self, nums: List[int]):
        self.dict = {idx:values for idx,values in enumerate(nums) if values != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        product = 0
        for i in self.dict:
            if i in vec.dict:
                product += self.dict[i] * vec.dict[i]
        return product
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)