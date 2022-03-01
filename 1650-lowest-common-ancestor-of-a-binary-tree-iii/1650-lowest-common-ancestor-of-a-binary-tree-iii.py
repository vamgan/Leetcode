class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        ptr_p, ptr_q = p, q
        while ptr_p is not ptr_q:
            ptr_p = ptr_p.parent if ptr_p.parent else q
            ptr_q = ptr_q.parent if ptr_q.parent else p
            
        return ptr_q
