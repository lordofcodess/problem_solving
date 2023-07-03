class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        c = [0] * 101  
        for x in nums:
            c[x] += 1
    
        p_sum = [0] * 101
        for i in range(1, 101):
            p_sum[i] = p_sum[i-1] + c[i-1]
    
        result = []
        for x in nums:
            result.append(p_sum[x])
    
        return result
