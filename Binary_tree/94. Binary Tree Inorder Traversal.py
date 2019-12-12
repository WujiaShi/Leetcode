class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode):
        if not root:
            return []
        res = []
        white, gray = 0, 1
        s = [(root, white)]
        
        while s:
            node, color = s.pop()
            if color == white:
                if node.right:
                    s.append((node.right, white))
                s.append((node, gray))
                if node.left:
                    s.append((node.left, white))
            else:
                res.append(node.val)
        return res