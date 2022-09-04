class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        def binarySearch(arr, target):
            left = 0
            right = len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return True
                if arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False
        for row in matrix:
            if target < row[0]:
                return False
            if target > row[cols - 1]:
                continue
            if target >= row[0] and target <= row[cols - 1]:
                return binarySearch(row, target)
            