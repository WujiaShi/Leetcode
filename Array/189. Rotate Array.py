
def rotate(nums, k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n
    print(k)
    nums[:] = nums[::-1]
    print(nums)
    nums[:k] = nums[:k][::-1]
    print(nums)
    nums[k:] = nums[k:][::-1]
    print(nums)

print(rotate([-1, -100, 3, 99], 2))

