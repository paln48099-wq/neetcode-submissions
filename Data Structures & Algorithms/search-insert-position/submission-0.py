class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        my_target = target+1
        low,high = 0,n-1
        lower_bound = n
        while low<=high:
            mid = (low+high)//2
            if nums[mid]>=my_target:
                high = mid-1
                lower_bound = mid
            else:
                low = mid+1
        return lower_bound
