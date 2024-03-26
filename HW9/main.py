class TreeNode(object):

     def __init__(self, val=0, left=None, right=None):

         self.val = val

         self.left = left

         self.right = right




class TreeNodeMain:
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None
        
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root
    
    def __init__(self):
        self.root = None

if __name__ == "__main__":
    tree = TreeNodeMain()

    tree.root = TreeNode(12)
    tree.root.left = TreeNode(8)
    tree.root.right = TreeNode(15)

    p = TreeNode(8)
    q = TreeNode(15)
    
    t = tree.lowestCommonAncestor(tree.root, p, q)
    
    print("LCA of", p.val, "and", q.val, "is", t.val)
