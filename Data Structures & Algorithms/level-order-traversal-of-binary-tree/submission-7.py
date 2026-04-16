# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        nodes = dict()
        max_level = 0
        def r_add(curr, level):
            nonlocal max_level
            if curr is None:
                return
            if level in nodes:
                nodes[level].append(curr.val)
            else:
                nodes[level] = [curr.val]
            r_add(curr.left, level+1)
            r_add(curr.right, level+1)
            max_level = max(level, max_level)
        r_add(root, 1)
        res = []
        for i in range(1, max_level+1):
            res.append(nodes[i])
        return res