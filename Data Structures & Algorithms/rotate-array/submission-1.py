class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums,k,left,right):
            if left>=right:
                return
            nums[left],nums[right] = nums[right],nums[left]
            reverse(nums,k,left+1,right-1)
        reverse(nums,k,0,len(nums)-1)
        reverse(nums,k,0,k-1)
        reverse(nums,k,k,len(nums)-1)
        return nums