class Solution:
    def searchRange(self, nums, target: int):
        if not nums:
            return [-1, -1]
        first_k = self.find_lower_bound(nums, target)
        if first_k == -1:
            return [-1, -1]
        last_k = self.find_upper_bound(nums, target)
        return [first_k, last_k]
    #notice how to caculate mid, by choosing different mid approach target number from
    #different side
    def find_lower_bound(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] != target:
            return - 1
        return left
    #
    def find_upper_bound(self, nums, target):
        left, right = 0, len(nums) -1
        while left < right:
            #notices
            mid = (left + right + 1) >> 1
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        if nums[left] != target:
            return -1
        return left