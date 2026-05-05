class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = -1
        rotten = list()
        rottenindex = 0
        freshexist = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                if grid[i][j] == 1:
                    freshexist = True
        if not freshexist:
            return 0
        curlen = len(rotten)
        while rottenindex < curlen:
            minutes+=1
            while rottenindex < curlen:
                i, j = rotten[rottenindex]
                rottenindex += 1
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
            curlen = len(rotten)
  
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return minutes