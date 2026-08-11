class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        l  = len(matrix)

        # Reverse the rows of the matrix
        for row in range(l):
            if row < l // 2:
                matrix[row], matrix[l - 1 - row] = matrix[l - 1 - row], matrix[row]
        

        for i in range(l):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        