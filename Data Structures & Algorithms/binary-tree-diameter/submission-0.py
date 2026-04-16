# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth_and_diameter(curr):
            if curr is None:
                return 0, 0
            if curr.left is None and curr.right is None:
                return 1, 0
            ldepth, ldiameter = depth_and_diameter(curr.left)
            rdepth, rdiameter = depth_and_diameter(curr.right)
            curr_diameter = ldepth + rdepth
            return 1 + max(ldepth, rdepth), max([curr_diameter, ldiameter, rdiameter])
        return depth_and_diameter(root)[1]

        