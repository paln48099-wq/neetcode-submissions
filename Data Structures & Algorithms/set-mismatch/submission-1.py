class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count =[0,0]
        n = len(nums)
        dict = {}
        for i in range(0,n):
          dict[nums[i]] = dict.get(nums[i],0) + 1
        for i in range(1,n+1):
          if dict.get(i,0) == 0:
            count[1] = i
          if dict.get(i,0) == 2 :
            count[0] = i
        return count

        