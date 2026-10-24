class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max = -1
        for i in range(n - 1, -1, -1):
            current = arr[i]         
            arr[i] = max
            if current > max:  
                max = current
        return arr