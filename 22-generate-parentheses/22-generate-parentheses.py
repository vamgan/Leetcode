class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(st,oc, openb, closeb):
            if closeb == n and openb == 0:
                print(st)
                res.append(st)
            if oc < n:
                helper(st + '(', oc + 1, openb + 1, closeb)
            if openb > 0:
                helper(st + ')', oc, openb - 1, closeb + 1)
        helper('', 0,0,0)
        return res