class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        
        def preorder(root):
            res = []
            if root:
                res += [str(root.val)]
                res += preorder(root.left)
                res += preorder(root.right)
            return res
        return ','.join(preorder(root))


    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        def build_tree(pre_o, in_o):
            if not pre_o:
                return None
            mid = pre_o[0]
            idx = in_o.index(mid)
            root = TreeNode(mid)
            root.left = build_tree(pre_o[1:idx + 1], in_o[:idx])
            root.right = build_tree(pre_o[idx + 1:], in_o[idx + 1:])
            return root
        pre_o = list(map(int, data.split(',')))
        in_o = sorted(pre_o)
        return build_tree(pre_o, in_o)
