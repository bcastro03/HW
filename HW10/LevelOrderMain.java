import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class LevelOrderMain {
	TreeNode root;

	public List<List<Integer>> levelOrder(TreeNode root) {
		Queue<TreeNode> queue = new LinkedList<>();
		List<List<Integer>> finalAns = new ArrayList<List<Integer>>();
		if (root == null) {
			return finalAns;
		}
		queue.add(root);
		while (!queue.isEmpty()) {
			int levels = queue.size();
			List<Integer> subLevels = new ArrayList<>();
			for (int i = 0; i < levels; i++) {
				if (queue.peek().left != null) {
					queue.add(queue.peek().left);
				}
				if (queue.peek().right != null) {
					queue.add(queue.peek().right);
				}
				subLevels.add(queue.remove().val);
			}
			finalAns.add(subLevels);
		}
		return finalAns;
	}

	public static void main(String[] args) {
		LevelOrderMain tree = new LevelOrderMain();
		tree.root = new TreeNode(18);
		tree.root.left = new TreeNode(8);
		tree.root.left.left = new TreeNode(7);
		tree.root.left.right = new TreeNode(9);
		tree.root.right = new TreeNode(15);
		tree.root.right.left = new TreeNode(14);
		tree.root.right.right = new TreeNode(16);
		List<List<Integer>> values = tree.levelOrder(tree.root);

		System.out.println(values);

	}

}
