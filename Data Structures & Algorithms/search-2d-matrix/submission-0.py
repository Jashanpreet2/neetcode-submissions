class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len = len(matrix[0])
        col_len = len(matrix)
        def get_num(index):
            return matrix[index//row_len][index % row_len]
        low = 0
        high = (row_len * col_len) - 1
        while low <= high:
            mid = (low + high) // 2
            mid_num = get_num(mid)
            if target < mid_num:
                high = mid - 1
            elif target > mid_num:
                low = mid + 1
            else:
                return True
        return False