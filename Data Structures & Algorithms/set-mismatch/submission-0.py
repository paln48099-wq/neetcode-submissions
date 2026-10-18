class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        output = []
        dict = {}
        n = len(nums)
        dup = 0
        missing = 0
      
        for i in range(0,n):
            dict[nums[i]] = dict.get(nums[i],0) + 1
        result = {str(i): dict.get(i, 0) for i in range(1, len(nums) + 1)}      
        for x,y in result.items():
            if y==2:
                dup = int(x)
            if y==0:
                missing = int(x)
        output.append(dup)
        output.append(missing)
        return output
        