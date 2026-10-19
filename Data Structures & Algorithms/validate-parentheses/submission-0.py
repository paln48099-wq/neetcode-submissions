class Solution:
    def isValid(self, s: str) -> bool:
        s1 = []
        for i in range(0,len(s1)-1):
            s1.append(s[i])
        left = 0 
        right = len(s1)-1
        
        while(left<right):
            s1[left],s1[right] = s1[right],s1[left]
            left+=1
            right-=1
        new = s1
        
      
        if new==s1:
            return True
        else:
            return False



       
       