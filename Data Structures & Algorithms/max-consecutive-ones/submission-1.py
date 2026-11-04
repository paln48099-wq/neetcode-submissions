class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max = float("-inf")
        n = len(nums)
        i=0
        while i<n: 
            while i<n and nums[i]==1:
                count+=1
                i+=1
            if count>max:
                max = count
                count = 0 
                i+=1
            else:
                i+=1
        return max