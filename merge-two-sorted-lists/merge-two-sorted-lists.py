# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        head = ListNode(None)
        p3 = head
        p2 = list2
        while p1 != None and p2 != None:
            if p1.val < p2.val:
                p3.next = p1
                p1 = p1.next
            else:
                p3.next = p2
                p2 = p2.next
            p3 = p3.next
        if p1 != None:
            p3.next = p1
        elif p2 != None:
            p3.next = p2
        return head.next
        