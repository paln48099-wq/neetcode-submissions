class Solution:
    def isValid(self, s: str) -> bool:
        s1 = []
        for i in range(0,len(s)-1):
            s1.append(s[i])
        original = s1
        left = 0 
        right = len(s1)-1
        
        while(left<right):
            s1[left],s1[right] = s1[right],s1[left]
            left+=1
            right-=1
        
        
        
        return original==s1



       
       