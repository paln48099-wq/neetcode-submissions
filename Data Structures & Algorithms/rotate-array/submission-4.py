class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        n = len(nums)
        l1 = nums[:n-k]
        l2 = nums[n-k:]
        nums[:] = l2+l1
