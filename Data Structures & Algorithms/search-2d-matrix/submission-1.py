class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_nums = len(matrix)
        col_nums = len(matrix[0])
        
        left = 0
        right = (row_nums * col_nums) - 1

        while left <= right:
            mid = (left + right) // 2

            row = mid // col_nums
            col = mid % col_nums

            if target == matrix[row][col]:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False