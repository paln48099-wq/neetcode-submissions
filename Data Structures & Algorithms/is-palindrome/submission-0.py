class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = "".join([c.lower() for c in s if c.isalnum()])
        l1 = []
        l = []
        for i in range(0,len(s1)):
            l1.append(s1[i]) 
            l.append(s1[i])

        def func(l,left,right):
           
            if left>=right:
               return
            l[left],l[right] = l[right],l[left]
            func(l,left+1,right-1)
            
        func(l,0,len(s1)-1)
        return l==l1
    