class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        links =  {i: set() for i in range(n)}
        for n1, n2 in edges:
            links[n1].add(n2)
            links[n2].add(n1)
        toCheck = [0]
        seen = set([0])
        count = 0
        while len(toCheck) > 0:
            count += 1
            cur = toCheck.pop()
            while len(links[cur]) > 0:
                link = links[cur].pop()
                if link in seen:
                    return False
                seen.add(link)
                links[link].remove(cur)
                toCheck.append(link)
        return count == n

        