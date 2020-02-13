import copy

def minimumTotal(triangle):
    dp = copy.deepcopy(triangle)

    for i in range(1, len(dp)):
        for j in range(i+1):
            if j == 0:
                dp[i][j] += dp[i-1][j]     
            if j> 0 and j == i:
                dp[i][j] += dp[i-1][j-1]
                
            elif (j > 0 and j < i):
                dp[i][j] += min(dp[i-1][j-1],dp[i-1][j])
    print(dp)
    print(triangle)
    return (min(dp[-1]))

def minimumTotal2(triangle):
    for i in range(len(triangle) - 1, 0, -1):
        for j in range(i):
            triangle[i - 1][j] += min(triangle[i][j], triangle[i][j + 1])
    return triangle[0][0]

tra = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

print(minimumTotal(tra))

