class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partition(n,low,high):
            pivot = n[low]
            i,j = low,high
            while i<j:
                while n[i]<=pivot and i<high:
                    i+=1
                while n[j]>pivot and j>low:
                    j-=1
                if i<j:
                    n[i],n[j] = n[j],n[i]
            n[low],n[j] = n[j],n[low]
            return j
        def quick_sort(n,low,high):
            if low<high:
                p_index = partition(n,low,high)
                quick_sort(n,low,p_index-1)
                quick_sort(n,p_index+1,high)
        return quick_sort(nums,0,len(nums)-1)