class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letter = ""
        for i in t:
            if i not in s and len(t) > len(s) :
                
                letter += i
            elif s.count(i) < t.count(i):
                letter = i
        return letter
