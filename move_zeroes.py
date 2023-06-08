class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        zeros_count = 0
        
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1
            else:
                zeros_count += 1
        while zeros_count > 0:
            nums[i] = 0
            i += 1
            zeros_count -= 1
