class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if s == "":
            return None
        if s[-1].isdigit():
            return TreeNode(int(s))
        idx = s.index('(')
        root = TreeNode(s[0:idx])
        j = idx + 1
        par = {'(', ')'}
        stack = [root]
        while j < len(s):
            if s[j] in par:
                if s[idx] == '(':
                    stack.append(TreeNode(s[idx+1:j]))
                if s[j] == ')':
                    node = stack.pop()
                    if stack[-1].left:
                        stack[-1].right = node
                    else:
                        stack[-1].left = node
                idx = j
            j += 1
        return root