class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.out = []
        self.dfs(root, 0)
        return self.out
    
    def dfs(self, node, depth):
        if node is None:
            return
        if len(self.out) == depth:
            self.out.append(node.val)
        self.dfs(node.right, depth + 1)
        self.dfs(node.left, depth + 1)