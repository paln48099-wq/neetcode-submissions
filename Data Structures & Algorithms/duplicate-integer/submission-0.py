class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        dict = {}
        for i in range(0,n):
            dict[nums[i]] = dict.get(nums[i],0)+1
        result = 2 in dict.values()
        return result