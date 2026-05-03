"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        added = set()
        maps = dict()
        nodes = list()
        beg = cur = Node(node.val, [])
        maps[beg.val] = beg
        nodes.extend(node.neighbors)
        while len(nodes) > 0:
            if node in added:
                node = nodes.pop()
                continue
            added.add(node)
            cur = maps[node.val]
            for n in node.neighbors:
                if n.val in maps.keys():
                    cur.neighbors.append(maps[n.val])
                else:
                    newNode = Node(n.val, [])
                    maps[n.val] = newNode
                    cur.neighbors.append(newNode)
            node = nodes.pop()
            nodes.extend(node.neighbors)
        return beg
