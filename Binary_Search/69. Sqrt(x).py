class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
            
        left, right = 0, (x // 2) + 1
        while left < right:
            mid = (left + right + 1) >> 1
            if mid * mid > x:
                right = mid -1
            else:
                left = mid
        return left

from math import e, log
class Solution1:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left = int(e**(0.5 * log(x)))
        right = left + 1
        return left if right * right > x else right
