class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        leftDiagonalTaken = [False for _ in range(2*n-1)]
        rightDiagonalTaken = [False for _ in range(2*n-1)]
        colTaken = [False for _ in range(n)]
        res = []
        board = []
        def recurse(row):
            for col in range(n):
                if colTaken[col] or leftDiagonalTaken[col-row+n-1] or rightDiagonalTaken[col+row-1]:
                    continue
                colTaken[col] = True
                leftDiagonalTaken[col-row+n-1] = True
                rightDiagonalTaken[col+row-1] = True
                board.append("."*(col)+"Q"+(n-col-1)*".")
                if row == n-1:
                    res.append(board.copy())
                else:
                    recurse(row+1)
                board.pop()
                colTaken[col] = False
                leftDiagonalTaken[col-row+n-1] = False
                rightDiagonalTaken[col+row-1]= False
        recurse(0)
        return res
