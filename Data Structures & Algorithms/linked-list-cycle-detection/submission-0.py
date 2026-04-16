# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        vals = set()
        while head is not None:
            if head.val in vals:
                return True
            vals.add(head.val)
            head = head.next
        return False
        