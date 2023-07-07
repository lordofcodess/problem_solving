class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        d = []
        for x in nums:
            st = str(x)
            reversed_num = int(st[::-1])
            d.append(reversed_num)

        for x in nums:
            d.append(x)
        unique_set = set()

        for x in d:
            unique_set.add(x)
        return len(unique_set)
