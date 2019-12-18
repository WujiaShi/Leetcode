
class Solution:
    def singleNumber(self, nums: [int]) -> int:
        ones, twos, threes = 0, 0, 0
        for num in nums:
            twos |= ones & num # 二进制某位出现1次时twos = 0，出现2, 3次时twos = 1；
            ones ^= num  # 二进制某位出现2次时ones = 0，出现1, 3次时ones = 1；
            threes = ones & twos # 二进制某位出现3次时（即twos = ones = 1时）three = 1，其余即出现1, 2次时three = 0；
            ones &= ~threes # 将二进制下出现3次的位置零，实现`三进制下不考虑进位的加法`；
            twos &= ~threes
        return ones

#用数学原理求解
class Solution2:
    def singleNumber(self, nums: [int]) -> int:
        if not nums:
            return
        num_set = set()
        for i in nums:
            if i not in num_set:
                num_set.add(i)
            else:
                continue
        sum_nums = sum(nums)
        sum_set = sum(num_set)
        a = 3* sum_set - sum_nums
        return int(a/2)
