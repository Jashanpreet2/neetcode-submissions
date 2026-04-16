class Solution:
    def maxArea(self, heights: List[int]) -> int:
        beg = 0
        end = len(heights) - 1
        maximum = 0
        while beg < end:
            current_storage = (end - beg) * (heights[beg] if heights[beg] < heights[end] else heights[end]) 
            if current_storage > maximum:
                maximum = current_storage
            if heights[beg] < heights[end]:
                beg += 1
            else:
                end -= 1
        return maximum


        