
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root != None:
            if root.left != None:
                pre = root.left
                while pre.right != None:
                    pre = pre.right
                pre.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
        return


def flatten_recursive(self, root: TreeNode):
        if root is None:
            return
        self.flatten_recursive(root.left)
        self.flatten_recursive(root.right)
        if root.left:
            pre = root.left
            while pre.right:
                pre = pre.right
            pre.right = root.right
            root.right = root.left
            root.left = None