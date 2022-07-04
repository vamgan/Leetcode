# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        resList = None
        while head:
            resList, resList.next = ListNode(head.val), resList
            head = head.next
        return resList