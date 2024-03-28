from collections import deque
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class LevelOrderMain:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        finalAns = []
        if not root:
            return finalAns
        queue = deque([root])
        while queue:
            levels = len(queue)
            subLevels = []
            for _ in range(levels):
                node = queue.popleft()
                subLevels.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            finalAns.append(subLevels)
        return finalAns

if __name__ == "__main__":
    tree = LevelOrderMain()
    tree.root = TreeNode(18)
    tree.root.left = TreeNode(8)
    tree.root.left.left = TreeNode(7)
    tree.root.left.right = TreeNode(9)
    tree.root.right = TreeNode(15)
    tree.root.right.left = TreeNode(14)
    tree.root.right.right = TreeNode(16)
    values = tree.levelOrder(tree.root)
    print(values)