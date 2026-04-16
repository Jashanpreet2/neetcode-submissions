# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        first = head
        while first is not None:
            length += 1
            first = first.next
        split_at = length//2
        secondhead = head
        i = 0
        while i < split_at:
            if i == split_at - 1:
                secondhead.next, secondhead = None, secondhead.next
            else:
                secondhead = secondhead.next
            i += 1 
        one = None
        second = secondhead
       
        while second is not None:
            second.next, second, one = one, second.next, second
            
        secondhead = one
        second = secondhead
        first = head
        while second is not None and first is not None:
            first.next, second.next, second, first = second, first.next if first.next is not None else second.next, second.next, first.next
    
        