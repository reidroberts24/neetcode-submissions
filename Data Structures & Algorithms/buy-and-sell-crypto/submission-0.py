class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        min_price = float("inf")

        for p in prices:
            if p < min_price:
                min_price = p
            
            if p > min_price:
                profit = max(profit, p - min_price)
        return profit