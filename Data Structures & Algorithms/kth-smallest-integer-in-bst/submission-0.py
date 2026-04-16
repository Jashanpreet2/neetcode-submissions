# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = 0
        def r(root) -> [int, bool]:
            if root is None:
                return None, False
            nonlocal curr
            lval, lfound = r(root.left)
            if lfound:
                return lval, True
            curr += 1
            if curr == k:
                return root.val, True
            rval, rfound = r(root.right)
            if rfound:
                return rval, True
            return None, False
        return r(root)[0]
            
