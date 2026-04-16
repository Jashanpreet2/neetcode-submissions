class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest_area = heights[0]
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                min = heights[i]
                for k in range(i, j+1):
                    min = min if min < heights[k] else heights[k]
                area = min * (j - i + 1)
                largest_area = area if area > largest_area else largest_area
        return largest_area
                
        