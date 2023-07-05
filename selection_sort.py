class Solution: 
    def select(self, arr, i):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        return min_idx
    
    def selectionSort(self, arr,n):
        for i in range(n - 1):
            s_idx = self.select(arr, i)
            arr[i], arr[s_idx] = arr[s_idx], arr[i]
