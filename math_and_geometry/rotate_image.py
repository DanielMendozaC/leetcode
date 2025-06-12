class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        # To rotate: You would need to move each element clockwise, how many positions?
        # Depends on where the element is located with respect to the center.

        # First transpose and then reverse the rows...
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Now reverse each row
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-1-j]  = matrix[i][-1-j], matrix[i][j]

        # Time complexity is O(N^2) and space complexity is O(1)


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Reverse the matrix vertically
        matrix.reverse()

        # Transpose the matrix
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]