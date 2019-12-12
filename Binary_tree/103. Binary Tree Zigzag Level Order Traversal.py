class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):  
        if not root:
            return []
        cur_level = [root]
        res = []
        left_to_right = True
        
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
            if left_to_right == True:
                res.append(tmp)
            else:
                res.append(tmp[::-1])
            left_to_right = not left_to_right
        return res