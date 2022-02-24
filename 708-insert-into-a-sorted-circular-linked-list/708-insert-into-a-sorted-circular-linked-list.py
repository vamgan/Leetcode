"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        newNode = Node(insertVal)
        insert = False
        if not head:
            newNode.next = newNode
            return newNode
        prev = head
        curr = head.next
        while True:
            if prev.val <= insertVal <= curr.val:
                insert = True
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    insert = True
            if insert:
                newNode.next = curr
                prev.next = newNode
                return head
            prev = curr
            curr = curr.next
            if prev == head:
                break
        newNode.next = curr
        prev.next = newNode
        
        return head