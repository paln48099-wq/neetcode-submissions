class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dict = {}
        
        for i in range(0,n):
            remaining = target - nums[i]
            if remaining in dict:
                return [dict[remaining],i]
            dict[nums[i]] = i