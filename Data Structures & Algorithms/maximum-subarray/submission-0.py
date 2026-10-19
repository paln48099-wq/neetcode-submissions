class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        high = []
        if len(nums)==1:
            return -1
        def func(left,right):
            sum = 0 
            i = left
            while i>=left and i<=right:
                sum = sum+nums[i]
                i+=1
            return sum
        
        for i in range(0,n):
            j = 1
            while j<n:
                high.append(func(i,j))
                j+=1
        return max(high)


    
            