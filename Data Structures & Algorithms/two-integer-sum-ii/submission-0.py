class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        dict = {}
        
        for i in range(0,n):
            remaining = target - numbers[i]
            if remaining in dict:
                return [numbers[dict[remaining]],numbers[i]]
            dict[numbers[i]] = i
         