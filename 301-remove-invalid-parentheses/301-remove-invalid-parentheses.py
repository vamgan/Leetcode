class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left = right = 0
        for c in s:
            if c == "(":
                left += 1
            elif c == ")":
                if left == 0:
                    right += 1
                else:
                    left -= 1
        self.ans = set()
        
        def dfs(depth, l, r, left, right, curr):
            if depth == len(s):
                if left == right == 0 and l == r:
                    self.ans.add(curr)
                    return
            else:
                if s[depth] == '(':
                    if left > 0:
                        dfs(depth + 1, l, r, left - 1, right, curr)
                    dfs(depth + 1, l + 1, r, left, right, curr + '(')
                elif s[depth] == ')':
                    if right > 0:
                        dfs(depth + 1, l, r, left, right - 1, curr)
                    if l > r:
                        dfs(depth + 1, l, r + 1, left, right, curr + ')')
                else:
                    dfs(depth + 1, l, r, left, right, curr + s[depth])
        dfs(0,0,0,left,right,'')
        return list(self.ans)
                    