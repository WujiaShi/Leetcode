class Solution:
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
                continue
            left, right = 0, len(dp) - 1
            while left < right:
                mid = (left + right) >> 1
                if dp[mid] < nums[i]:
                    left = mid + 1
                else: 
                    right = mid
            dp[left] = nums[i]
        return len(dp)