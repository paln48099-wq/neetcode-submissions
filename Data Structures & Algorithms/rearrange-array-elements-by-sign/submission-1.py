class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p = 0
        q = 1 
        l =[0]*n
        for i in range(0,n):
            if nums[i]<=0:
                l[q] = nums[i]
                q+=2
            else:
                l[p] = nums[i]
                p+=2
        return l