class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for i in range(0,len(nums)):
            dict[nums[i]] = dict.get(nums[i],0) + 1
        max_key = max(dict, key=dict.get)
        return max_key