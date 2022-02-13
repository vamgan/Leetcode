# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        r,c = binaryMatrix.dimensions()[0], binaryMatrix.dimensions()[1]
        x,y = 0,c-1
        left_most = c
        while x < r and y >= 0:
            if binaryMatrix.get(x,y) == 1:
                if y < left_most:
                    left_most = y
                y -= 1
            else:
                x += 1
        
        return left_most if left_most != c else -1