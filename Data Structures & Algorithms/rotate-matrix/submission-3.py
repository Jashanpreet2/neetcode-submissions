class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        size = len(matrix)
        for n in range(0, len(matrix)//2+1):
            for i in range(size-2*n-1):
                tl=(n, n+i)
                tr=(n+i, size-n-1)
                br=(size-n-1, size-n-1-i)
                bl=(size-n-1-i, n)
                matrix[tl[0]][tl[1]], matrix[tr[0]][tr[1]], matrix[br[0]][br[1]], matrix[bl[0]][bl[1]] = matrix[bl[0]][bl[1]], matrix[tl[0]][tl[1]], matrix[tr[0]][tr[1]], matrix[br[0]][br[1]]
    