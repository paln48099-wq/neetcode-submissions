class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
      
        def func(left,right):
            sum = 0 
            i = left
            while i>=left and i<=right:
                sum = sum+nums[i]
                i+=1
            return sum
        max_value = nums[0]
        for i in range(0,n):
            j = i
            while j<n:
                current_sum = func(i,j)
                if current_sum>max_value:
                    max_value = current_sum
                j+=1
        return max_value     
            