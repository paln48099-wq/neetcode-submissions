class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # RECURSIVE SOLUTION 
        n = len(nums)
        def bs(n,low,high):
            if low>high:
                return -1
            mid = (low+high)//2
            if n[mid]==target:
                return mid
            elif n[mid]<target:
                return bs(n,mid+1,high)
            else:
                return bs(n,low,mid-1)
        return  bs(nums,0,n-1)
        
