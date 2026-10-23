class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
      
        
        n = len(nums)
        result = 0 
        count = nums[0]
        for i in range(0,n):
            if nums[i] == k :
                result+=1
            count = nums[i]
            for j in range(i+1,n):
                if count+nums[j] == k:
                    result+=1
                    count = count+nums[j]
                else:
                    count = nums[j]+count
        return result              



        