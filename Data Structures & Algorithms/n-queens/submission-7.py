class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        leftDiagonalTaken = [False for _ in range(2*n-1)]
        rightDiagonalTaken = [False for _ in range(2*n-1)]
        colTaken = [False for _ in range(n)]
        cols = set([i for i in range(n)])
        res = []
        board = []
        done = set()
        def recurse(row):
            for col in cols:
                # if row == 0 and col in done:
                #     continue
                if colTaken[col] or leftDiagonalTaken[col-row+n-1] or rightDiagonalTaken[col+row-1]:
                    continue
                colTaken[col] = True
                leftDiagonalTaken[col-row+n-1] = True
                rightDiagonalTaken[col+row-1] = True
                board.append("." * (col)+"Q"+(n-col-1)*".")
                if row == n-1:
                    res.append(board.copy())
                    # if n > 1:
                    #     res.append(board[::-1].copy())
                    #     done.add(col)
                else:
                    recurse(row+1)
                board.pop()
                colTaken[col] = False
                leftDiagonalTaken[col-row+n-1] = False
                rightDiagonalTaken[col+row-1]= False
        recurse(0)
        return res
