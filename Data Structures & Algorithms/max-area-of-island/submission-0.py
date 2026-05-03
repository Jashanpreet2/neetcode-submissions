class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        used = set()
        def getArea(i, j):
            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or grid[i][j] == 0 or (i, j) in used:
                    return 0
            used.add((i, j))

            # toget = list()
            # toget.append((i-1, j), (i+1, j))
            # for i, j in toget:

            return 1+ getArea(i-1, j)+getArea(i+1, j) + getArea(i, j-1) + getArea(i, j+1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in used:
                    continue
                area = getArea(i, j)
                maxArea = max(area, maxArea)

        return maxArea        