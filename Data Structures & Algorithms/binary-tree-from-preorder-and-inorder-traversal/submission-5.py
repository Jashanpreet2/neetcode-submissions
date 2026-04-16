# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        length = 1
        def add(left, right):
            if right < left:
                return None
            nonlocal length
            toAdd = preorder[length]
            length += 1
            j = 0
            while inorder[j] != toAdd:
                j += 1
            node = TreeNode(toAdd)
            node.left = add(left, j-1)
            node.right = add(j+1, right)
            print(node.val, node.right.val if node.right else "a")
            return node
        j = 0
        while inorder[j] != root.val:
            j += 1
        root.left = add(0, j-1)
        root.right = add(j+1, len(inorder)-1)
        return root
