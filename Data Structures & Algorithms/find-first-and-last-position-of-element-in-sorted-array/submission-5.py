class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def lower_bound(nums,target):
            low,high,lb = 0,n-1,n
            while low<=high :
                mid = (low+high)//2
                if nums[mid]>=target:
                    high = mid-1
                    lb = mid
                else:
                    low = mid+1
            return lb
        def upper_bound(nums,target):
            low,high,ub = 0,n-1,n
            while low<=high :
                mid = (low+high)//2
                if nums[mid]>target:
                    high = mid-1
                    ub = mid
                else:
                    low = mid+1
            return ub
        first = lower_bound(nums, target)

        # Target not present in array
        if first == n or nums[first] != target:
            return [-1, -1]

        last = upper_bound(nums, target)
        return [first, last - 1]
                
