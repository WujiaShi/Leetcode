from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        max_num=nums[0]
        right=0
        for i in range(n):
            if(nums[i]>=max_num):
                max_num=nums[i]
            else:
                right=i
        left=n
        min_num=nums[-1]
        for i in range(n-1,-1,-1):
            if(nums[i]<=min_num):
                min_num=nums[i]
            else:
                left=i
        return right-left+1 if(right-left+1 >0) else 0


def findUnsortedSubarray(nums: List[int]) -> int:
    if not nums:
        return 0
    cur_min, cur_max = nums[-1], nums[0]
    n = len(nums)
    start, end = n, 0
    
    for i in range(1, n):
        if nums[i] >= cur_max:
            cur_max = nums[i]
            print("cur_max", cur_max)
        else:
            end = i - 1
            print("end", end)
            break
    print("i", i)

    for j in range(n-1, 0, -1):
        if nums[j] <= cur_min:
            cur_min = nums[j]
            print("cur_min", cur_min)
        else:
            start = j + 1
            print("start,", start)
            break
    print("j", j)

    return end - start + 1

nums = [1,2,3,4]
print(findUnsortedSubarray(nums))