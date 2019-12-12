class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []
        cur_level = [root]
        res = []
        
        while cur_level:
            next_level = []
            tmp = []
            for node in cur_level:
                tmp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            cur_level = next_level
            res.append(tmp)
        bottom_up = []
        while res:
            bottom_up.append(res.pop())
        return bottom_up