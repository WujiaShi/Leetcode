class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def __init__(self):
        self.res = []

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.preorder(root)
        return (",").join(self.res)
        
    def preorder(self, root):
        if not root:
            self.res.append("#")
            return 
        self.res.append(str(root.val))
        self.preorder(root.left)
        self.preorder(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        d = iter(data.split(","))
        
        def construct():
            tmp = next(d)
            if tmp == "#":
                return 
            node = TreeNode(int(tmp))
            node.left = construct()
            node.right = construct()
            return node
        
        return construct()