# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def r_get_min_and_max_and_validity(root):
            if root is None:
                return None, None, True
            l_min_value, l_max_value, lvalid = r_get_min_and_max_and_validity(root.left)
            r_min_value, r_max_value, rvalid = r_get_min_and_max_and_validity(root.right)
            validity = lvalid and rvalid and (not l_max_value or root.val > l_max_value) and (not r_min_value or root.val < r_min_value)
            return l_min_value or root.val, r_max_value or root.val, validity
        return r_get_min_and_max_and_validity(root)[2]
        

        