class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maximum = float("-inf")
        current_sum = 0 
        for i in range(0,n):
            current_sum = current_sum + nums[i]
            if current_sum > maximum:
                maximum = current_sum
            if current_sum<0:
                current_sum = 0 
        return maximum

            
