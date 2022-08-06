# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode(None)
        res = head
        while l1 or l2:
            if l1 and l2:
                num = l1.val + l2.val + carry
                carry = num // 10
                dig = num % 10
                res.next = ListNode(dig)
                res = res.next
                l1 = l1.next
                l2 = l2.next
            elif l1 and not l2:
                num = l1.val + carry
                carry = num // 10
                dig = num % 10
                res.next = ListNode(dig)
                res = res.next
                l1 = l1.next
            elif l2 and not l1:
                num = l2.val + carry
                carry = num // 10
                dig = num % 10
                res.next = ListNode(dig)
                res = res.next
                l2 = l2.next
        if carry != 0:
            res.next = ListNode(carry)
        return head.next