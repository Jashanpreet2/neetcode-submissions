# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levelscovered = 0
        visible = []
        def rview(root, level):
            if root is None:
                return
            nonlocal levelscovered
            if level > levelscovered:
                visible.append(root.val)
                levelscovered = level
            rview(root.right, level + 1)
            rview(root.left, level + 1)
        rview(root, 1)
        return visible
        