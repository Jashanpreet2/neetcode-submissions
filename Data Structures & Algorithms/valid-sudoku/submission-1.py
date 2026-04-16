class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        quads = []
        for i in range(3):
            quads.append([])
            for j in range(3):
                quads[i].append(set())

        rows = [None] * 9
        cols = [None] * 9
        for i in range(9):
            rows[i] = set()
            cols[i] = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                val = board[i][j]
                if val == ".":
                    continue
                if val in quads[i // 3][j // 3] or val in rows[i] or val in cols[j]:
                    return False
                quads[i // 3][j // 3].add(val)
                rows[i].add(val)
                cols[j].add(val)
        return True
        