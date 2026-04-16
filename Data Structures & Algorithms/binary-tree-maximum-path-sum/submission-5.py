# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def get_val(node):
            if node is None:
                return -1001
            leftval = get_val(node.left)
            rightval = get_val(node.right)
            node.asleafval = node.val + (node.left.asleafval if node.left and node.left.asleafval > 0 and (not node.right or node.left.asleafval > node.right.asleafval) else node.right.asleafval if node.right and node.right.asleafval > 0 else 0)
            print(node.val, node.left.asleafval if node.left else 0, node.right.asleafval if node.right else 0)

            node.val = node.val + (0 if not node.left or node.left.asleafval < 0 else node.left.asleafval) + (0 if not node.right or node.right.asleafval < 0 else node.right.asleafval)
            return max(node.val, leftval, rightval)
        return get_val(root)