class Solution(object):
    def smallestEvenMultiple(self, n):
      if n % 2 == 0:
         return n
      else:
         n = n * 2
         return n
