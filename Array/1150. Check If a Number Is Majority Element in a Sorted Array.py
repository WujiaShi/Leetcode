class Solution:
    def isMajorityElement(self, nums, target: int) -> bool:
        if not nums:
            return False
        length = len(nums)
        mid = length >> 1
        if nums[mid] == target:
            return self.check_validity(nums, target)
        else:
            return False
        
    def check_validity(self, nums, elem):
        freq = 0
        for num in nums:
            if num == elem:
                freq += 1
        if len(nums) < freq *2:
            return True
        return False