class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1 = {}
        for i in range(0,len(s)):
            dict1[s[i]] = dict1.get(s[i],0)+1
        for x,y in enumerate(s):
            if dict1[y]==1:
              return x
              
        return(-1)
        