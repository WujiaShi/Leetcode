class Solution:
    def permuteUnique(self, nums):
        if not nums:
            return []
        res = []
        nums.sort()
        used = [False] * len(nums)
        self.dfs(nums, 0, [], used, res)
        return res
        
    def dfs(self, nums, idx, permute, used, res):
        if idx == len(nums):
            res.append(permute.copy())
            return
        
        for i in range(len(nums)):
            if used[i] == False:
                if (i > 0 and nums[i] == nums[i-1] and used[i-1] == False):
                    continue
                permute.append(nums[i])
                used[i] = True

                self.dfs(nums, idx + 1, permute, used, res)
                used[i] = False
                permute.pop()