class Solution:
    def reverse(self, x: int) -> int:
        
       
        def convert(x):
            sum =0
            while (x>0):
                last_digit = x%10
                sum = sum*10+last_digit
                x = x//10
                if sum > 2147483647:
                    return 0
            return sum
        if x<0 :
            if x < -2147483648:
                return 0
            x = -(x)
            return -(convert(x))
        else:
            if x > 2147483648:
                return 0
            return convert(x)
               
       