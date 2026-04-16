"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        new = Node(head.val, None, new if head.next is head else None)
        d = dict()
        d[head] = new
        headcopy = head
        newcopy = new
        while headcopy.next is not None:
            newcopy.next = Node(headcopy.next.val, None, None)
            d[headcopy.next] = newcopy.next
            headcopy = headcopy.next
            newcopy = newcopy.next
        headcopy = head
        newcopy = new
        while headcopy is not None:
            newcopy.random = d[headcopy.random] if headcopy.random is not None else None
            headcopy = headcopy.next
            newcopy = newcopy.next
        return new
