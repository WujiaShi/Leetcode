class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [[[0]*2 for _ in range(3)] for _ in range(n)]
        # dp[i][j][0]表示第i天交易了j次时不持有股票, dp[i][j][1]表示第i天交易了j次时持有股票
        # 定义卖出股票时交易次数加1
        for i in range(3):
            dp[0][i][0], dp[0][i][1] = 0, -prices[0]
        
        for i in range(1, n):
            for j in range(3):
                if not j:
                    dp[i][j][0] = dp[i-1][j][0]
                else:
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j][0] - prices[i])
        
        return max(dp[n-1][0][0], dp[n-1][1][0], dp[n-1][2][0])