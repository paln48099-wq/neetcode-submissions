class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return 0
        if n==1:
            return 1
        def merge_array(left,right):
            i,j = 0,0
            n,m = len(left),len(right)
            result = []
            while i<n and j<m :
                if left[i]<=right[j]:
                    result.append(left[i])
                    i+=1
                else:
                    result.append(right[j])
                    j+=1
            if i<n:
                while i<n:
                    result.append(left[i])
                    i+=1
            if j<m :
                while j<m :
                    result.append(right[j])
                    j+=1
            return result


        def merge_sort(nums):
            if len(nums)<=1:
                return nums 
            mid = len(nums)//2
            left_half = nums[:mid]
            right_half = nums[mid:]
            left = merge_sort(left_half)
            right = merge_sort(right_half)
            return merge_array(left,right)
        nums = merge_sort(nums)
        max_value = 1
        count = 1
        for i in range(1,n):
        
            if nums[i]==nums[i-1]+1:
                count+=1
            elif nums[i]==nums[i-1]:
                continue
            else:
                max_value = max(max_value,count)
                count = 1
            max_value = max(max_value,count)
        return max_value       
       
        