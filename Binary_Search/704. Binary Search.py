class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right ) >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if target == nums[left]:
            return left
        else:
            return -1