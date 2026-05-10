class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        orig_pacifics = [(0, j) for j in range(len(heights[0]))] + [(i, 0) for i in range(len(heights))]
        orig_atlantics = [(len(heights)-1, j) for j in range(len(heights[0]))] + [(i, len(heights[0])-1) for i in range(len(heights))]
        fpacifics = set()
        fatlantics = set()
        def backtrack(spots, s):
            def addIfOkay(i, j, height):
                if i >= 0 and i < len(heights) and j >= 0 and j < len(heights[0]) and (i, j) not in s and heights[i][j] >= height:
                    s.add((i, j))
                    spots.append((i, j))
            k = 0
            while k < len(spots):
                i, j = spots[k]
                height = heights[i][j]
                if (i, j) not in s:
                    s.add((i, j))
                addIfOkay(i-1, j, height)
                addIfOkay(i+1, j, height)
                addIfOkay(i, j-1, height)
                addIfOkay(i, j+1, height)
                k+=1
        backtrack(orig_pacifics, fpacifics)
        backtrack(orig_atlantics, fatlantics)
        res = []
        for spot in fpacifics:
            if spot in fatlantics:
                res.append(spot)
        return res

