class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dict = {}
        n = len(nums)
        
        for i in range(0,n):
            dict[nums[i]] = dict.get(nums[i],0) + 1 
        for i in range(1,n+2):
            if dict.get(i,0) == 0 :
                return i 
               