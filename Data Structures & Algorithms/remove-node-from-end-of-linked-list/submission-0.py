# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        length = 0
        cur = head
        while cur is not None:
            length += 1
            cur = cur.next
        cur = head
        toremove = length - n
        if n == length:
            return head.next
        i = 0
        while i < length:
            if i == toremove - 1:
                cur.next = cur.next.next
                return head
            cur = cur.next
            i += 1
