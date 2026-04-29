# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        slow, fast = head, head.next
        while fast != None:
            if fast.next is None or fast.next.next is None:
                return False
            if fast.next == slow or fast.next.next == slow:
                return True
            slow, fast = slow.next, fast.next.next
        return  False