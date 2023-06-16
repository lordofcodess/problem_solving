class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        num_deleted_columns = 0
        n = len(strs)
        m = len(strs[0])  

        for j in range(m):  
            for i in range(1, n): 
                if strs[i][j] < strs[i-1][j]:  
                    num_deleted_columns += 1
                    break  

        return num_deleted_columns
