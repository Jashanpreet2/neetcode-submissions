class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def setDist(i, j, dist):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == -1 or grid[i][j] == 0:
                return
            print(dist, grid[i][j])
            if dist <= grid[i][j]:
                grid[i][j] = dist
                setDist(i-1, j, dist+1)
                setDist(i+1, j, dist+1)
                setDist(i, j-1, dist+1)
                setDist(i, j+1, dist+1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    setDist(i-1, j, 1)
                    setDist(i+1, j, 1)
                    setDist(i, j-1, 1)
                    setDist(i, j+1, 1)