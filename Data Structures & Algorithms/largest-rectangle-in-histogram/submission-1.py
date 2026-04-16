class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = []
        indexes = []
        largest = heights[0]
        for i in range(len(heights)):
            oldest = i
            while len(l) > 0 and l[-1] > heights[i]:
                l.pop()
                oldest = indexes.pop()
            if len(l) == 0 or heights[i] != l[-1]:
                l.append(heights[i])
                indexes.append(oldest)
            for j in range(len(l)):
                area = l[j] * (i - indexes[j] + 1)
                if area > largest:
                    largest = area
        return largest
                
        