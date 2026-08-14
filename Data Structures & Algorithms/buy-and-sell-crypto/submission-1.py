class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy low, sell high
        if len(prices) < 2:
            return 0
        buy_day, sell_day = 0, 1
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < prices[buy_day]:
                buy_day = i
            
            cur_profit = prices[i] - prices[buy_day]
            if cur_profit > max_profit:
                sell_day = i
                max_profit = cur_profit
        return max_profit

            