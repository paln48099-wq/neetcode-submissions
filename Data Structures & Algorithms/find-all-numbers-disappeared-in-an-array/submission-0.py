class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dict = {}
        result = []
        n = len(nums)
        for num in nums:
            dict[num] = 1
        for i in range(1,n+1):
            if dict.get(i,0)== 0 :
                result.append(i)
        return result