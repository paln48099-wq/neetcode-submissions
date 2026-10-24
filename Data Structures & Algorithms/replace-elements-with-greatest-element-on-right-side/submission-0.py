class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)

        def greatest(nums):
            largest = float("-inf")
            for num in nums:
                if num>largest:
                    largest = num
            return largest
        for i in range(0,n):
            
            l1 = arr[i+1:n]
            
            highest = greatest(l1)
            if highest == float("-inf"):
                arr[i] = -1
            else:
                arr[i] = highest
        return arr
    
