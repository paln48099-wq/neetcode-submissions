class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = 0 
        n = len(nums)
        for i in range(0,n):
            if nums[i]!=val:
                nums[i],nums[p] = nums[p],nums[i]
                p+=1
        return p 
        return nums