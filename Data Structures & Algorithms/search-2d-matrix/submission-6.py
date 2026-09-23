class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top = 0
        bottom = len(matrix) - 1
        row = 0
        
        while top <= bottom:
            middle = top+(bottom - top)//2
            if matrix[middle][0] > target:
                bottom = middle - 1
            elif matrix[middle][0] <= target:
                top = middle + 1
            else:
                break
        row = bottom


        print(row)
        left = 0
        right = len(matrix[0])-1
        while left <= right:
            middle = left+(right - left)//2
            if matrix[row][middle] > target:
                right = middle - 1
            elif matrix[row][middle] < target:
                left = middle + 1
            else:
                return True

        return False
