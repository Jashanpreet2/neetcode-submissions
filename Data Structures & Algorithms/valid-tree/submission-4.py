class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        links =  {i: set() for i in range(n)}

        for n1, n2 in edges:
            links[n1].add(n2)
            links[n2].add(n1)

        toCheck = [0]

        while len(toCheck) > 0:
            cur = toCheck.pop()
            n -= 1
            while len(links[cur]) > 0:
                link = links[cur].pop()
                links[link].remove(cur)
                toCheck.append(link)

        return n == 0

        