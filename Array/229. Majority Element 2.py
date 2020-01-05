class Solution:
    def majorityElement(self, nums):
        if not nums:
            return []
        if len(nums) == 1:
            return nums
        c1 = c2 = None
        freq_c1 = freq_c2 = 0
        
        for num in nums:
            if num == c1:
                freq_c1 += 1
            elif num == c2:
                freq_c2 += 1
            elif freq_c1 == 0:
                c1 = num
                freq_c1 = 1
            elif freq_c2 == 0:
                c2 = num
                freq_c2 = 1
            else:
                freq_c1 -= 1
                freq_c2 -= 1
        return self.check_validity(nums, c1, c2)
        
    def check_validity(self, nums, c1, c2):
        res = []
        f1, f2 = 0, 0
        for num in nums:
            if num == c1:
                f1 += 1
            elif num == c2:
                f2 += 1
        if f1 * 3 > len(nums):
            res.append(c1)
        if f2 * 3 > len(nums):
            res.append(c2)
        return res
                