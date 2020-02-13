def maximalRectangle(mat) -> int:
    if not mat:
        return 0
    row, col = len(mat), len(mat[0])
    dp = [[0 for _ in range(col)] for _ in range(row)]
    #fill the first row and col in dp array
    for i in range(col):
        dp[0][i] = int(mat[0][i])
    for i in range(row):
        dp[i][0] = int(mat[i][0])
    
    for i in range(1, row):
        for j in range(1, col):
            if mat[i][j] == '1':
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
            else:
                dp[i][j] = 0
    print(dp)
    #find the fisrt and second max values in dp
    a, b = 1, 0
    for i in range(row):
        for j in range(col):
            if dp[i][j] > a:
                b = a
                a = dp[i][j]
            elif a > dp[i][j] > b:
                b = dp[i][j]
            else:
                continue
    return a*b

mat = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

print(maximalRectangle(mat))