class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cur = 0
        curcells = set()
        def backtrack(i, j):
            nonlocal cur
            if board[i][j] != word[cur] or (i, j) in curcells:
                return False
            curcells.add((i, j))
            cur += 1
            if cur == len(word):
                return True
            if j < len(board[0]) - 1 and backtrack(i, j + 1):
                return True
            if j > 0 and backtrack(i, j - 1):
                return True
            if i < len(board) - 1 and backtrack(i+1, j):
                return True
            if i > 0 and backtrack(i - 1, j):
                return True
            cur -= 1
            curcells.remove((i, j))
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j):
                    return True
        return False
        