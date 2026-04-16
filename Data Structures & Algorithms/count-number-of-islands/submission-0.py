class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        processed = set()
        count = 0

        def check_around(i1, j1):
            if (i1, j1) in processed:
                return
            if grid[i1][j1] == "0":
                return

            processed.add((i1, j1))
            if i1 > 0:
                check_around(i1 - 1, j1)
            if i1 < len(grid) - 1:
                check_around(i1 + 1, j1)
            if j1 > 0:
                check_around(i1, j1 - 1)
            if j1 < len(grid[i]) - 1:
                check_around(i1, j1 + 1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in processed:
                    check_around(i, j)
                    count += 1

        return count


        