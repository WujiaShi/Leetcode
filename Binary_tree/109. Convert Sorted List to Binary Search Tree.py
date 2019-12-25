class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head) -> TreeNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.recursive(nums)
    
    def recursive(self, nums):
        if not nums:
            return None
        left = 0
        right = len(nums) - 1
        if left > right:
            return None
        mid = (left + right) >> 1
        root = TreeNode(nums[mid])
        root.left = self.recursive(nums[left:mid])
        root.right = self.recursive(nums[mid + 1: right+1])
        return root