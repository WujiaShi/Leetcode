class Solution:
    def twoSum(self, nums, target: int):
        if not nums:
            return []
        dic = {}
        for idx, num in enumerate(nums):
            if target - num in dic:
                return [dic[target - num], idx]
            else:
                dic[num] = idx


