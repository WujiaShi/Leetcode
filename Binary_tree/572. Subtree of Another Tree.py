class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        if not s:
            return False

        return self.check_sub(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
                
    def check_sub(self, root1, root2):
        if not root2 and not root1:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return self.check_sub(root1.left, root2.left) and self.check_sub(root1.right, root2.right) 