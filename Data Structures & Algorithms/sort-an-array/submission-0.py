class Solution:
    def merge_array(self,left,right):
        i,j = 0,0 
        n,m = len(left),len(right)
        result = []
        while i<n and j<m:
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
        if j<m:
            while j<m:
               result.append(right[j])
               j+=1
        return result

    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums)<=1:
            return nums
        mid = len(nums)//2
        left_half = nums[:mid]
        right_half = nums[mid:]
        left = self.sortArray(left_half)
        right = self.sortArray(right_half)
        return self.merge_array(left,right)
        
      

        