class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root: TreeNode):
        if not root:
            return []
        
        res = defaultdict(list)
        queue = deque()
        queue.append((root, 0))
        
        while queue:
            node, level = queue.popleft()
            res[level].append(node.val)
            if node.left:
                queue.append((node.left, level - 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        return [res[x] for x in sorted(res.keys())]
        
        