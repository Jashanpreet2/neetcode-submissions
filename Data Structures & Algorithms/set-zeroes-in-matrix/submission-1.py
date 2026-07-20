class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.add(j)
                    cols.add(i)
        for row in rows:
            for i in range(len(matrix)):
                matrix[i][row] = 0
        for col in cols:
            for j in range(len(matrix[col])):
                matrix[col][j] = 0
        
        