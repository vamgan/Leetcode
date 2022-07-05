# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lengthL = 0
        llp = head
        while llp:
            lengthL += 1
            llp = llp.next
        mid = lengthL // 2
        print(mid)
        for i in range(1, mid + 1):
            head = head.next
        return head
            