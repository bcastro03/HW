
public class TreeNodeMain {

	TreeNode root;

	public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {

		if (root == null)
			return null;

		if (root.val > p.val && root.val > q.val)

			return lowestCommonAncestor(root.left, p, q);

		if (root.val < p.val && root.val < q.val)

			return lowestCommonAncestor(root.right, p, q);

		return root;
	}

	public static void main(String[] args) {

		TreeNodeMain tree = new TreeNodeMain();

		tree.root = new TreeNode(12);

		tree.root.left = new TreeNode(8);
		
		tree.root.right = new TreeNode(15);

		TreeNode p = new TreeNode(8);
		
		TreeNode q = new TreeNode(15);
		
		TreeNode t = tree.lowestCommonAncestor(tree.root, p, q);
		
		System.out.println("LCA of " + p.val + " and " + q.val + " is " + t.val);

	}
}