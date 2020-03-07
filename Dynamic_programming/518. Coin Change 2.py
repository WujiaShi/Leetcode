class Solution:
    def change(self, amount: int, coins) -> int:
        size = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(size + 1)]
        dp[0][0] = 1

        for i in range(1, size + 1):
            for j in range(amount + 1):
                dp[i][j] += dp[i - 1][j]
                if j - coins[i - 1] >= 0:
                    dp[i][j] += dp[i][j - coins[i - 1]]
        return dp[size][amount]