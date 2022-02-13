```
class SparseVector:
def __init__(self, nums: List[int]):
self.dict = {idx:values for idx,values in enumerate(nums) if values != 0}
​
def dotProduct(self, vec: 'SparseVector') -> int:
product = 0
for i in self.dict:
if i in vec.dict:
product += self.dict[i] * vec.dict[i]
return product
```