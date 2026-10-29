class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0 
        l1 = []

        for char in s:
            ascii_value = ord(char)
            l1.append(ascii_value)
        n = len(l1)
        for i in range(1,n):
            substract =  l1[i] - l1[i-1]
        
            if substract<0:
                sum =  sum - substract
            else:
                sum = sum + substract
        return sum