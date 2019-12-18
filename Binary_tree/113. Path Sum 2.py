class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#solve recursively
class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        if not root:
            return []
        res = []
        self.valid_path(root, sum, res, [])
        return res
    
    def valid_path(self, root, target, res, path):
        if not root:
            return
        if not root.left and not root.right and root.val == target:
            path.append(root.val)
            res.append(path)
        
        self.valid_path(root.left, target - root.val, res, path + [root.val])
        self.valid_path(root.right, target - root.val, res, path+ [root.val])

#solve iteratively        
class Solution2:
    def pathSum(self, root: TreeNode, sum_: int):
        if not root: return []
        stack = [([root.val], root)]
        res = []
        while stack:
            tmp, node = stack.pop()
            if not node.right and not node.left and sum(tmp) == sum_:
                res.append(tmp)
            if node.right:
                stack.append((tmp + [node.right.val], node.right))
            if node.left:
                stack.append((tmp + [node.left.val], node.left))
        return res