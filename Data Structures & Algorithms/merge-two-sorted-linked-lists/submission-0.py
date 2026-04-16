# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            new = list1
            list1 = list1.next
        else:
            new = list2
            list2 = list2.next
        head = new
        while list1 is not None or list2 is not None:
            if list1 is None and list2 is not None:
                new.next = list2
                list2 = list2.next; print("As1")
            elif list2 is None and list1 is not None:
                new.next = list1
                list1 = list1.next
            elif list2.val <= list1.val:
                new.next = list2
                list2 = list2.next; print("As2")
            else:
                new.next = list1
                list1 = list1.next
            new = new.next
        return head
        