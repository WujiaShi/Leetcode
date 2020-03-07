class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        max_profit, buy = 0, prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            cur_profit = prices[i] - buy
            max_profit = max(cur_profit, max_profit)
        return max_profit