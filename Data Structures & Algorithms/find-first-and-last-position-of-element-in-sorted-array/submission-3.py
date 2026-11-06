class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        if n == 1:
            if nums[0]==target:
                return [0,0]
            else:
                return [-1,-1]

        def lower_bound():
            low,high,lb,ub = 0,n-1,-1,-1
            while low<=high :
                mid = (low+high)//2
                if nums[mid]>=target:
                    high = mid-1
                    lb = mid
                else:
                    low = mid+1
            return lb
        def upper_bound():
            low,high,lb,ub = 0,n-1,-1,-1
            while low<=high :
                mid = (low+high)//2
                if nums[mid]>target:
                    high = mid-1
                    ub = mid
                else:
                    low = mid+1
            if ub==-1:
                ub = 0 
                return ub
            else:
                return ub
        first,last = lower_bound(),upper_bound()-1
        return [first,last]
        

                
