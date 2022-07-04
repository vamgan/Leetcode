class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        LEFT_BOUND, RIGHT_BOUND = len(s), len(t)
        
        def isSub(left_index, right_index):
            if left_index == LEFT_BOUND:
                return True
            if right_index == RIGHT_BOUND:
                return False
            if s[left_index] == t[right_index]:
                left_index += 1
            right_index += 1
            return isSub(left_index, right_index)
        return isSub(0,0)