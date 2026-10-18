class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        result = []
        n = len(nums)
        i=0
        while i<n: 
            while i<n and nums[i]==1:
                count+=1
                i+=1
            result.append(count)
            count = 0 
            i+=1
        max = result[0]
        for num in result:
            if num>max:
                max = num
        return max   