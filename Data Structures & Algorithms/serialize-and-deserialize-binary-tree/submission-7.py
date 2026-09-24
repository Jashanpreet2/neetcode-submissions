# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        out = []
        to_add = [root]
        i = 0
        while i < len(to_add):
            curNode = to_add[i]
            i += 1
            out.append(str(curNode.val) if curNode is not None else "None")
            if curNode is not None:
                to_add.append(curNode.left)
                to_add.append(curNode.right)
        return ",".join(out)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        nodes = [TreeNode(int(val)) if val != "None" else None for val in data.split(",")]
        i = 0
        nextNodeIndex = 1
        for i, node in enumerate(nodes):
            if node == None:
                continue
            if nextNodeIndex >= len(nodes):
                break
            if nextNodeIndex < len(nodes):
                node.left = nodes[nextNodeIndex]
            nextNodeIndex += 1 
            if nextNodeIndex < len(nodes):
                node.right = nodes[nextNodeIndex]
            nextNodeIndex += 1
            i += 1
        return nodes[0]





