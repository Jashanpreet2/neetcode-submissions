class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rowlen, collen = len(grid[0]), len(grid)
        seen = set()
        toCheck = list()
        def check(i, j):
            if grid[i][j] == "0" or (i, j) in seen:
                return
            seen.add((i, j))
            if i-1 >= 0:
                toCheck.append((i-1, j))
            if i+1 < collen:
                toCheck.append((i+1, j))
            if j-1 >= 0:
                toCheck.append((i, j-1))
            if j+1 < rowlen:
                toCheck.append((i, j+1))
            
        for i in range(collen):
            for j in range(rowlen):
                if (i, j) in seen or grid[i][j] == "0":
                    continue
                count += 1
                check(i, j)
                while len(toCheck) > 0:
                    c = toCheck.pop()
                    check(c[0], c[1])
        return count

    