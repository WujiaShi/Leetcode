class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.check_symmetric(root, root)
        
    def check_symmetric(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return self.check_symmetric(root1.left, root2.right) and self.check_symmetric(root1.right, root2.left)
        