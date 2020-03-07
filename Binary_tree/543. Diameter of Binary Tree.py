class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def __init__(self):
        self.max = 0
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.depth(root)
         
        return self.max
        
    def depth(self, root):
        if not root:
            return 0
        l = self.depth(root.left)
        r = self.depth(root.right)
        '''每个结点都要去判断左子树+右子树的高度是否大于self.max，更新最大值'''
        self.max = max(self.max, l+r)
        
        # 返回的是高度
        return max(l, r) + 1