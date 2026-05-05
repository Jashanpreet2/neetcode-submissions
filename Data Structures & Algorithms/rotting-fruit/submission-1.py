class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = -1
        rotten = list()
        freshexist = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                if grid[i][j] == 1:
                    freshexist = True
        if not freshexist:
            return 0
        while len(rotten) > 0:
            minutes+=1
            curlen = len(rotten)
            while curlen > 0:
                i, j = rotten.pop(0)
                curlen -= 1
                if i-1 >= 0 and grid[i-1][j] == 1:
                    rotten.append((i-1, j))
                    grid[i-1][j] = 2
                if i+1 < len(grid) and grid[i+1][j] == 1:
                    rotten.append((i+1, j))
                    grid[i+1][j] = 2
                if j-1 >= 0 and grid[i][j-1] == 1:
                    rotten.append((i, j-1))
                    grid[i][j-1] = 2
                if j+1 < len(grid[0]) and grid[i][j+1] == 1:
                    rotten.append((i, j+1))
                    grid[i][j+1] = 2
  
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return minutes