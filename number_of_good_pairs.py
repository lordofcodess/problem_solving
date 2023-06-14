class Solution(object):
    def numIdenticalPairs(self, nums):
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        count = 0
        for freq in frequency.values():
            if freq >= 2:
                count += freq * (freq - 1) // 2

        return count
