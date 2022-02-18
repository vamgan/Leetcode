
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        answer = Node(head.val, None, head.random)
        answerHead = answer
        mapper = {head:answer}
        while head.next:
            answer.next = Node(head.next.val, None, head.next.random)
            mapper[head.next] = answer.next
            head = head.next
            answer = answer.next
        answer = answerHead
        while answer:
            if answer.random:
                answer.random = mapper[answer.random]
            answer = answer.next
        return answerHead