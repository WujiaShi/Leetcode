class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max = float('-inf')
        self.max_path(root)
        return self.max
        
    def max_path(self, root):
        if not root: 
            return 0
        
        left = self.max_path(root.left)
        right = self.max_path(root.right)
        
        self.max = max(left + right + root.val, self.max)
        tmp = max(left, right) + root.val
        return tmp if tmp > 0 else 0

