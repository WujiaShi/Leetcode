class Solution:
    def majorityElement(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        target = nums[0]
        freq = 1
        for i in range(1, len(nums)):
            if freq == 0:
                target = nums[i]
                freq = 1
            elif nums[i] == target:
                freq += 1
            else:
                freq -= 1
        return target