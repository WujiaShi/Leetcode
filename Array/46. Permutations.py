class Solution:
    def permute(self, nums):
        if not nums:
            return []
        used = [False] * len(nums)
        res = []
        self.dfs(nums, [], 0, used, res)
        return res
        
    def dfs(self, nums, permute, idx, used, res):
        if idx == len(nums):
            res.append(permute.copy())
            return
        for i in range(len(nums)):
            if used[i] == False:
                permute.append(nums[i])
                used[i] = True
                self.dfs(nums, permute, idx + 1, used, res)
                permute.pop()
                used[i] = False