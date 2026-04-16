# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def r_is_balanced(root):
            if root is None:
                return True, 0
            if root.left is None and root.right is None:
                return True, 1
            lbalanced, ldepth = r_is_balanced(root.left)
            rbalanced, rdepth = r_is_balanced(root.right)
            return lbalanced and rbalanced and abs(ldepth - rdepth) <= 1, 1 + max(ldepth, rdepth)
        return r_is_balanced(root)[0]
            