# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:    
        def isSame(r1, r2):
            if bool(r1) != bool(r2):
                return False
            
            if r1 is None and r2 is None:
                return True
            
            if r1.val == r2.val:
                return isSame(r1.left, r2.left) and isSame(r1.right, r2.right)
            
            return False

        if isSame(root, subRoot):
            return True
        if root.left:
            return self.isSubtree(root.left, subRoot)
        if root.right:
            return self.isSubtree(root.right, subRoot)

        return False
        
        