class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        if n == 1:
            return [0,0]
        def lower_bound():
            low,high,lb,ub = 0,n-1,n,n
            while low<=high :
                mid = (low+high)//2
                if nums[mid]>=target:
                    high = mid-1
                    lb = mid
                else:
                    low = mid+1
            return lb
        def upper_bound():
            low,high,lb,ub = 0,n-1,n,n
            while low<=high :
                mid = (low+high)//2
                if nums[mid]>target:
                    high = mid-1
                    ub = mid
                else:
                    low = mid+1
            return ub
        first,last = lower_bound(),upper_bound()-1
        return [first,last]
        

                
