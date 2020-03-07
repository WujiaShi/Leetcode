class Solution:
    def findDisappearedNumbers(self, nums):
        res = []
        if not nums:
            return res
        
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
                
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
                
        return res