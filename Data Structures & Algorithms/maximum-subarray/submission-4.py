class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_value = float("-inf")
        for i in range(0,n):
            total = 0 
            for j in range(i,n):
                total = total + nums[j]
                max_value = max(max_value,total)
        return max_value