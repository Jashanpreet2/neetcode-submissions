class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        links = dict([i, set()] for i in range(n))
        allNodes = set([i for i in range(n)])
        for e1, e2 in edges:
            links[e1].add(e2)
            links[e2].add(e1)
        groups =  0
        def clearLinks(node):
            while len(links[node]) > 0:
                link = links[node].pop()
                links[link].remove(node)
                if link in allNodes:
                    allNodes.remove(link)
                clearLinks(link)
        while len(allNodes) > 0:
            groups += 1
            node = allNodes.pop()
            clearLinks(node)

        return groups