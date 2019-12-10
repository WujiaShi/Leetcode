class Solution:
    def generateMatrix(self, n: int):
        if not n :
            return []
        mat = [[0 for _ in range(n)] for _ in range(n)]
        
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        a = 1
        
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                mat[top][i] = a
                a += 1
            top += 1
            if top > bottom:
                break
            
            for i in range(top, bottom + 1):
                mat[i][right] = a
                a += 1
            right -= 1
            if left > right:
                break
            
            for i in range(right, left - 1, -1):
                mat[bottom][i] = a
                a += 1
            bottom -= 1
            
            for i in range(bottom, top - 1, -1):
                mat[i][left] = a
                a += 1
            left += 1
            
        return mat