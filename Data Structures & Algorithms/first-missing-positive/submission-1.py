class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dict = {}
        n = len(nums)
        if n==1:
            return n+1
        for i in range(0,n):
            dict[nums[i]] = dict.get(nums[i],0) + 1 
        for i in range(1,n+1):
            if dict.get(i,0) == 0 :
                return i 
               