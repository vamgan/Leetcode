```
class Solution:
def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
r,c = binaryMatrix.dimensions()[0], binaryMatrix.dimensions()[1]
idx = c
for row in range(r):
x = self.binaryHelper(binaryMatrix,row,0,c - 1)
if x is not None and x < idx:
idx = x
return idx if idx != c else -1
def binaryHelper(self, binaryMatrix,row,left,right):
if left > right:
return None
mid = (left + right) //2
if binaryMatrix.get(row,mid) == 1:
if mid == 0 or binaryMatrix.get(row,mid-1) == 0:
return mid
if binaryMatrix.get(row,mid) == 0:
return self.binaryHelper(binaryMatrix, row,mid + 1,right)
else:
return self.binaryHelper(binaryMatrix, row,left,mid - 1)
r,c = binaryMatrix.dimensions()[0], binaryMatrix.dimensions()[1]