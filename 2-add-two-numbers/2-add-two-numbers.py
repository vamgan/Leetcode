# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def convert_to_num(node):
            string = ""
            while node.next:
                string  = str(node.val) + string
                node = node.next
            string  = str(node.val) + string
            return int(string)
        l1_num = convert_to_num(l1)
        l2_num = convert_to_num(l2)
        res = str(l1_num + l2_num)[::-1]
        head = ListNode(None) 
        node_res = head
        for i in res:
            node_res.next = ListNode(i)
            node_res = node_res.next
        return head.next
            