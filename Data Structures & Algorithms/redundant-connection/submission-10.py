class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        goesTo = dict()
        for edge in edges:
            e1, e2 = edge
            if e1 not in goesTo:
                goesTo[e1] = set()
            if e2 not in goesTo:
                goesTo[e2] = set()
            goesTo[e1].add(e2)
            goesTo[e2].add(e1)
        
        cyclicEdges = set()
        
        def amICyclic(seenNodesSet, seenNodesList, curNode, comingFrom):
            if curNode in seenNodesSet:
                cyclicEdges.add((curNode, comingFrom))
                for i in range(len(seenNodesList)-2, -1, -1):
                    edge = (seenNodesList[i+1], seenNodesList[i])
                    cyclicEdges.add(edge)
                    if seenNodesList[i] == curNode:
                        return True
            seenNodesSet.add(curNode)
            seenNodesList.append(curNode)
            for nextNode in goesTo[curNode]:
                if nextNode == comingFrom:
                    continue
                if amICyclic(seenNodesSet, seenNodesList, nextNode, curNode):
                    return True
            seenNodesSet.remove(curNode)
            seenNodesList.pop()

        amICyclic(set(), list(), edges[0][0], None)
        print(cyclicEdges)
        for i in range(len(edges)-1, -1, -1):
            e1, e2 = edges[i]
            if (e1, e2) in cyclicEdges or (e2, e1) in cyclicEdges:
                return edges[i]
