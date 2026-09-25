# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur is not None:
            length += 1
            cur = cur.next
        times = length//k
        res = None
        needsNext = None

        prev = None
        cur = head
        next = cur.next

        for _ in range(times):
            willNeedNext = cur
            for i in range(k):
                cur.next = prev
                prev = cur
                cur = next
                next = cur.next if cur is not None else cur
            if res is None:
                res = prev
            if needsNext is not None:
                needsNext.next = prev
            needsNext = willNeedNext
        needsNext.next = cur
        return res
        
        
        
        