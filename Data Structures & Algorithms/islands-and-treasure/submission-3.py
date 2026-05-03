class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        todo = list()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    todo.append((i, j))
        while len(todo) > 0:
            i, j = todo.pop(0)
            if i == 1:
                print(i, j)
            if i-1 >= 0 and grid[i-1][j] == INF and grid[i-1][j] not in [0, -1]:
                grid[i-1][j] = grid[i][j] + 1
                todo.append((i-1, j))
            if i+1 < len(grid) and grid[i+1][j] == INF and grid[i+1][j] not in [0, -1]:
                grid[i+1][j] = grid[i][j] + 1
                todo.append((i+1, j))
            if j-1 >= 0 and grid[i][j-1] == INF and grid[i][j-1] not in [0, -1]:
                grid[i][j-1] = grid[i][j] + 1
                todo.append((i, j-1))
            if j+1 < len(grid[0]) and grid[i][j+1] == INF and grid[i][j+1] not in [0, -1]:
                grid[i][j+1] = grid[i][j] + 1
                todo.append((i, j+1))