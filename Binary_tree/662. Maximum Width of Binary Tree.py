
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = [(root, 0, 0)]
        max_width, left, cur_depth = 0, 0, 0
        
        for node, depth, pos in queue:
            if node:
                queue.append((node.left, depth + 1, pos *2))
                queue.append((node.right, depth + 1, pos *2 + 1))
                if cur_depth != depth:
                    cur_depth = depth
                    left = pos
                max_width = max(max_width, pos - left + 1)
        return max_width
 