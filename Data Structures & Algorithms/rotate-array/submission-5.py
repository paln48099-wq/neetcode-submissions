class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        def reverse(nums,k,left,right):
            while left<right:
                nums[left],nums[right] = nums[right],nums[left]
                left+=1
                right-=1

            
        reverse(nums,k,0,len(nums)-1)
        reverse(nums,k,0,k-1)
        reverse(nums,k,k,len(nums)-1)
        return nums