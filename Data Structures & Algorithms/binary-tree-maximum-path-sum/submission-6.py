# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = float('-inf')

        def max_gain(node) -> int:
            if not node:
                return 0
            left  = max(max_gain(node.left), 0)
            right = max(max_gain(node.right), 0)
            # best path through this node (can't be passed upward as a fork)
            self.best = max(self.best, node.val + left + right)
            # return the best single arm for the parent to build on
            return node.val + max(left, right)

        max_gain(root)
        return self.best