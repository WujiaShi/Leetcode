class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if not nums:
            return None
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
                
        if nums[left] >= target:
            return left
        elif nums[left] < target:
            return left + 1
