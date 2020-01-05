class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        size = len(nums)

        target = size - k
        left = 0
        right = size - 1
        while True:
            index = self.__partition(nums, left, right)
            if index == target:
                return nums[index]
            elif index < target:
                left = index + 1
            else:
                right = index - 1

    #  循环不变量：[left + 1, j] < pivot
    #  (j, i) >= pivot
    def __partition(self, nums, left, right):

        pivot = nums[left]
        j = left
        for i in range(left + 1, right + 1):
            if nums[i] < pivot:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[left], nums[j] = nums[j], nums[left]
        return j