from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        num_set = set()
        count = 0
        
        for num in arr:
            if num == 0:
                count += 1
                if count > 1:
                    return True
                continue
            
            if num * 2 in num_set or num / 2 in num_set:
                return True
            
            num_set.add(num)
        
        return False
