class Solution:
    def maxSubArray(self, nums) -> int:
        if not nums:
            return None
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i] + dp[i-1], nums[i])
        return max(dp)

class Solution2:
    def maxSubArray(self, nums):
        cur_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            cur_sum = max(nums[i], cur_sum + nums[i])
            max_sum = max(max_sum, cur_sum)
            
        return max_sum

class Solution3:
    def maxSubArray(self, nums):
        n = len(nums)
        max_sum = nums[0]
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1] 
            max_sum = max(nums[i], max_sum)

        return max_sum

