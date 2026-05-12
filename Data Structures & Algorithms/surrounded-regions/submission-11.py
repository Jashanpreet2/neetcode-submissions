class Solution:
    def solve(self, board: List[List[str]]) -> None:
        safeset = set()
        safeset.update([(i, 0) for i in range(len(board)) if board[i][0] == "O"])
        safeset.update([(i, len(board[0])-1) for i in range(len(board)) if board[i][-1] == "O"])
        safeset.update([(0, j) for j in range(1, len(board[0])-1) if board[0][j]=="O"])
        safeset.update([(len(board)-1, j) for j in range(1, len(board[0])-1) if board[-1][j] == "O"])
        safe = list(safeset)
        def addIfOkay(i, j):
            if i > 0 and i < len(board) and j > 0 and j < len(board[0]) and board[i][j] == "O" and (i, j) not in safeset:
                safeset.add((i, j))
                safe.append((i, j))
        k = 0
        while k < len(safe):
            i, j = safe[k]
            addIfOkay(i-1,j)
            addIfOkay(i+1,j)
            addIfOkay(i,j-1)
            addIfOkay(i,j+1)
            k+=1
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i, j) not in safeset:
                    board[i][j] = "X"

        