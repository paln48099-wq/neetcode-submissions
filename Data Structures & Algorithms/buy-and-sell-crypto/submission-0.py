class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_value = 0 
        for i in range(0,n):
            current_sum = 0 
            for j in range(i+1,n):
                if prices[i]<prices[j]:
                    current_sum = prices[j]-prices[i]
                if current_sum>max_value:
                    max_value=current_sum
        return max_value