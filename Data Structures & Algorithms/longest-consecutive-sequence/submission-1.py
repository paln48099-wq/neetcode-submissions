class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        numsNew = nums.sort()
        max_value = 1
        count = 1
        for i in range(1,n):
        
            if nums[i]==nums[i-1]+1:
                count+=1
            elif nums[i]==nums[i-1]:
                continue
            else:
                max_value = max(max_value,count)
                count = 1
            max_value = max(max_value,count)
        return max_value 