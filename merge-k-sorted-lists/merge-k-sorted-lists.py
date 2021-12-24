# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        if len(lists) == 0:
            return None
        p = head
        p.next = lists[0]
        for l in range(1, len(lists)):
            x = lists[l]
            p1 = head
            while x != None and p1.next != None:
                if p1.next.val > x.val:
                    temp = p1.next
                    p1.next = x
                    x = x.next
                    p1.next.next = temp
                else:
                    p1 = p1.next
            if x != None:
                p1.next = x
        return head.next