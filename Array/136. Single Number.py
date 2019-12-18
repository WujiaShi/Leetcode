
class Solution:
    def singleNumber(self, nums) -> int:
        number=0
        # 遍历数组，对数组中的每个元素进行 异或运算
        for i in range(len(nums)):
            number ^= nums[i]
        # 最终的number就是出现了一次的元素	
        return number