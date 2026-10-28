class Solution:
    def isPalindrome(self, x: int) -> bool:
        actual = x
        total = 0 
        while(x>0):
            last_digit = x%10
            total = (total*10)+ last_digit
            x = x // 10 
        if total == actual:
            return True
        else:
            return False   
