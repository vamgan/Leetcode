class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        return n == 3 ** round(math.log(n, 3))
        