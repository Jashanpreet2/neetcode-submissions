# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        nxt = head.next
        prev = None
        while head is not None:
            head.next = prev
            prev = head
            head = nxt
            nxt = head.next if head else None
        return prev