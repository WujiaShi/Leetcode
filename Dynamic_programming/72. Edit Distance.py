class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and not word2:
            return 0
        elif word2 and not word1:
            return len(word2)
        elif word1 and not word2:
            return len(word1)
        
        len1, len2 = len(word1), len(word2)
        dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
        
        for j in range(1, len2 + 1):
            dp[0][j] = dp[0][j-1] + 1
        for i in range(1, len1 + 1):
            dp[i][0] = dp[i-1][0] + 1
            
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
        return dp[-1][-1]