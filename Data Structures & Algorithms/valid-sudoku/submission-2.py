class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for rownum, row in enumerate(board):
            for colnum, value in enumerate(row):
                if value == '.':
                    continue
                if value in rows[rownum] or value in cols[colnum] or value in boxes[(rownum // 3) * 3 + colnum // 3]:
                    return False
                rows[rownum].add(value)
                cols[colnum].add(value)
                boxes[(rownum // 3) * 3 + colnum // 3].add(value)
        
        return True