# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = float("-inf")
        def get_max(node):
            if node is None:
                return 0
            leftval = get_max(node.left)
            rightval = get_max(node.right)
            self.best = max(self.best, node.val + leftval + rightval)
            return max(0, node.val + max(leftval, rightval))
        get_max(root)
        return self.best