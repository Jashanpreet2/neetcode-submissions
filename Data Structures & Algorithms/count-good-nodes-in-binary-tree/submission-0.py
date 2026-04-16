# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num_good = 0
        def r_goodNodes(root1, greatest):
            if root1 is None:
                return
            nonlocal num_good
            if root1.val >= greatest:
                num_good += 1
                greatest = root1.val
            r_goodNodes(root1.left, greatest)
            r_goodNodes(root1.right, greatest)
        r_goodNodes(root, root.val)
        return num_good
        