class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l = []
        l1 = []
        l3 =[]
        n = len(nums)
        for i in range(0,n):
            if nums[i]<0:
                l.append(nums[i])
            else:
                l1.append(nums[i])
        for i in range(0,(n//2)):
            l3.append(l1[i])
            l3.append(l[i])
        return l3    