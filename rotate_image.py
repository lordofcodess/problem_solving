class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        m = len(matrix)
        for i in range(m):
            for j in range(i, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        
        for i in range(m):
            matrix[i] = matrix[i][::-1]
