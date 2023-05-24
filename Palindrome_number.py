class Solution:
    def isPalindrome(self, x):
       
        x_str = str(x)
        
        
        return x_str == x_str[::-1]

checker = Solution()
print(checker.isPalindrome(121))  
print(checker.isPalindrome(-121))  
print(checker.isPalindrome(10)) 
