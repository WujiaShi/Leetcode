from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return None
        max_res = float("-inf")
        cur_max, cur_min = 1, 1
        for i in range(len(nums)):
            if nums[i] < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(nums[i], cur_max * nums[i])
            cur_min = min(nums[i], cur_min * nums[i])
            max_res = max(cur_max, max_res)
        return max_res