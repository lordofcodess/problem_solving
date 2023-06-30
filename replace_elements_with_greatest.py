class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:      
        n = len(arr)
        max_value = arr[n-1]  
        arr[n-1] = -1  
    
        for i in range(n-2, -1, -1):
            temp = arr[i]  
            arr[i] = max_value 
            max_value = max(max_value, temp)  
    
        return arr
