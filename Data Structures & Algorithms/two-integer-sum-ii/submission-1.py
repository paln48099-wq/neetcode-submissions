class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        dict = {}
        
        for i in range(0,n):
            remaining = target - numbers[i]
            if remaining in dict:
                return [dict[remaining]+1,i+1]
            dict[numbers[i]] = i
         