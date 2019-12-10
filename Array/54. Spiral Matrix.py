class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        row, column = len(matrix), len(matrix[0])
        left, right = 0, column - 1
        top, bottom = 0, row - 1
        res = []
        
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if top > bottom:
                break

            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if left > right:
                break

            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res