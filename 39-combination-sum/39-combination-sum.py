class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        def backtrack(candidate, arr, s):
            if s == target:
                self.ans.append(arr)
                return
            if s > target:
                return
            for i in range(len(candidate)):
                backtrack(candidate[i:], arr + [candidate[i]], s + candidate[i])
        backtrack(candidates,[], 0)
        return self.ans