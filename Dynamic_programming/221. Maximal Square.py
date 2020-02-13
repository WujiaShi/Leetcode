class Solution1:
    #dynamic programming
    def maximalSquare(self, matrix) -> int:
        if not matrix:
            return 0
        row, col = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        #fill the first row and col in dp array
        for i in range(col):
            dp[0][i] = int(matrix[0][i])
        for i in range(row):
            dp[i][0] = int(matrix[i][0])
        
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] = 0
        #find the maximum value in dp
        res = 0
        for i in range(row):
            for j in range(col):
                res = max(dp[i][j], res)
        return res*res

class Solution2:
    #space complexity reduced
    def maximalSquare(self, matrix) -> int:
        if not matrix:
            return 0
        row, col = len(matrix), len(matrix[0])
        dp = [0] * (col + 1)

    
        res, pre = 0, 0
        for i in range(row):
            for j in range(1, col + 1):
                cur = dp[j]
                if matrix[i][j - 1] == '1':
                    dp[j] = min(dp[j-1], dp[j], pre) + 1
                    res = max(dp[j], res)
                else:
                    dp[j] = 0
                pre = cur
            pre = 0
        return res*res