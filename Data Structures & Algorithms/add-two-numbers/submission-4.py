# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        root = l1
        lastnode = l1
        while l1 is not None and l2 is not None:
            l1.val, carry = (l1.val + l2.val + carry) % 10, (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
            lastnode = l1 if l1 is not None else lastnode
       
        if l1 is None and l2 is None:
            if carry > 0:
                lastnode.next = ListNode(carry)
            return root

        node = l1 if l1 is not None else l2
        if l2 is not None:
            lastnode.next = l2
            lastnode = node
            
        while carry != 0 and node != None:
            node.val, carry = (node.val + carry) % 10, (node.val + carry) // 10
            node = node.next
            lastnode = node if node is not None else lastnode

        if carry != 0:
            lastnode.next = ListNode(carry)

        return root
