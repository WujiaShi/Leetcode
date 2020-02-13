class Solution:
    def threeSum(self, nums):
        if not nums:
            return []
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            L = i + 1
            R = len(nums) - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1
                    L += 1
                    R -= 1
                elif nums[i] + nums[L] + nums[R] > 0:
                    R -= 1
                else:
                    L += 1
        return res


# solution 2: iterate over the array and split it into 3 dictionaries which contain postive
# numbers, negative numbers, and zero. Then the feasible solutions can be 2 postive + 1 negative,
# 2 negative + 1 postive, and 1 positive + 1 negative + 0.

import itertools
class Solution2:
    def threeSum(self, nums):
        if not nums:
            return []
        res, pos, neg, zero = [], {}, {}, 0
        for i in nums:
            if i > 0:
                if i not in pos:
                    pos[i] = 1
                else:
                    pos[i] += 1
            elif i < 0:
                if i not in neg:
                    neg[i] = 1
                else:
                    neg[i] += 1
            else:
                zero += 1
        if zero >= 3:
            res.append([0, 0, 0])
        
        for b, c in itertools.combinations_with_replacement(pos.keys(), 2):
            if b == c and pos[b] < 2:
                continue
            k = -(b + c)
            if k in neg.keys():
                res.append([b, c, k])
        
        for b, c in itertools.combinations_with_replacement(neg.keys(), 2):
            if b == c and neg[b] < 2:
                continue
            k = abs(b + c)
            if k in pos.keys():
                res.append([b, c, k])
        
        for a in pos.keys():
            if -a in neg.keys():
                if zero != 0:
                    res.append([a, 0, -a])
        return res