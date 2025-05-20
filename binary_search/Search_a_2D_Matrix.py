class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary search to find the correct row - O(log m)
        left_m = 0
        right_m = len(matrix)-1

        while left_m < right_m:
            middle_m = (right_m + left_m) // 2
            
            if target > matrix[middle_m][-1]:
                # Target is greater than all elements in current row, look in lower half
                left_m = middle_m + 1
            elif target < matrix[middle_m][0]:
                # Target is smaller than all elements in current row, look in upper half
                right_m = middle_m - 1
            else:
                # Target may be in this row, we found our row
                left_m = middle_m
                right_m = middle_m
        
        # Binary search within the identified row - O(log n)
        left_r = 0 
        right_r = len(matrix[right_m]) - 1

        while left_r <= right_r:
            middle_r = (right_r + left_r) // 2

            if target > matrix[right_m][middle_r]:
                left_r = middle_r + 1
            elif target < matrix[right_m][middle_r]:
                right_r = middle_r - 1
            else:
                return True  # Target found
        
        return False  # Target not found
        
        # Overall time complexity: O(log m + log n)
        # Where m = number of rows, n = number of columns
        
        # # Alternative solution with time complexity of O(m*n)
        # for row in matrix:
        #     for v in row:
        #         if v == target:
        #             return True
        # return False