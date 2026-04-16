# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        f = head.next
        s = head
        while f is not None:
            if s == f:
                return True
            s = s.next
            f = None if f.next is None else f.next.next
        return False
        