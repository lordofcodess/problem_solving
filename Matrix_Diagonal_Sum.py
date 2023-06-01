class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
     
        n = len(mat) 
        dia_sum = 0

        for i in range(n):
            dia_sum += mat[i][i] 
            
            if i != n - 1 - i:
                dia_sum += mat[i][n - 1 - i]
        
        return dia_sum
