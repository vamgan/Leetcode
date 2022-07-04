# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        resList = ListNode()
        head = resList
        while list1 and list2:
            if list1.val < list2.val:
                resList.next = ListNode(list1.val)
                resList = resList.next
                list1 = list1.next
            else:
                resList.next = ListNode(list2.val)
                resList = resList.next
                list2 = list2.next
        if list1:
            resList.next = list1
        else:
            resList.next = list2
        return head.next
                