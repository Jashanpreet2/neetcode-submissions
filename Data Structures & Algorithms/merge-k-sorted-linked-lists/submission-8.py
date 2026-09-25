# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = []
        counter = 0

        for head in lists:
            if head is not None:
                heapq.heappush(l, (head.val, counter, head))
                counter += 1

        if len(l) == 0:
            return None

        root = cur = heapq.heappop(l)[2]
        while len(l) > 0:
            if cur.next is not None:
                heapq.heappush(l, (cur.next.val, counter, cur.next))
                counter += 1
            nextNode = heapq.heappop(l)[2]
            cur.next = nextNode
            cur = cur.next

        return root
                    
        