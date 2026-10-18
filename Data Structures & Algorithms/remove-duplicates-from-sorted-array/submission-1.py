class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if nums==[]:
            return 0 
        if n==1:
            return 1
        p = 1

        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                nums[p]=nums[i]
                p+=1
        return p