# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        addrset = set()
        while head:
            if head in addrset:
                return head
            else:
                addrset.add(head)
            head = head.next
