class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        my_target = target+1
        low,high = 0,n-1
        pos = n 
        while low<=high:
            mid = (low+high)//2
            if nums[mid]<target:
                low = mid+1
            elif nums[mid]==target:
                pos = mid
                high = mid-1
            else:
                pos = mid
                high = mid-1
        return pos
            


