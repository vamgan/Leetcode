class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.longest_nodes = []
        self.helper(root)

        for node in self.longest_nodes:
            print(node.val)

        return len(self.longest_nodes) - 1
        
    def helper(self, root):
        if not root:
            return (0, [])
        
        left, left_nodes = self.helper(root.left)
        right, right_nodes = self.helper(root.right)
        
        if (left + right) > len(self.longest_nodes)-1:
            self.longest_nodes = left_nodes + [root] + right_nodes[::-1]

        if left > right:
            return (left+1, left_nodes + [root])
        else:
            return (right+1, right_nodes + [root])