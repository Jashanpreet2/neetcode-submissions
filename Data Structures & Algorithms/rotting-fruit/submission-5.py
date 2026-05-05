class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = -1
        rotten = list()
        rottenindex = 0
        totalFresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                if grid[i][j] == 1:
                    totalFresh += 1
        if totalFresh == 0:
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
                    totalFresh -= 1
                if i+1 < len(grid) and grid[i+1][j] == 1:
                    rotten.append((i+1, j))
                    grid[i+1][j] = 2
                    totalFresh -= 1
                if j-1 >= 0 and grid[i][j-1] == 1:
                    rotten.append((i, j-1))
                    grid[i][j-1] = 2
                    totalFresh -= 1
                if j+1 < len(grid[0]) and grid[i][j+1] == 1:
                    rotten.append((i, j+1))
                    grid[i][j+1] = 2
                    totalFresh -= 1
            curlen = len(rotten)
        return minutes if totalFresh == 0 else -1