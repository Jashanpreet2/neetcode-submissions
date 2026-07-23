class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        intervals.sort(key=lambda x: (x[0], x[1]))
        res = []
        def consuming(i1, i2):
            return i1[0] <= i2[0] and i1[1] >= i2[1]
        def overlapping(i1, i2):
            return i1[1] > i2[0]
        toAdd, i = 0, 1
        while i < len(intervals):
            while i < len(intervals):
                overlaps = overlapping(intervals[toAdd], intervals[i])
                consumes = consuming(intervals[toAdd], intervals[i])
                if consumes:
                    toAdd = i
                elif not overlaps:
                    break
                i += 1
            res.append(intervals[toAdd])
            toAdd = i
        return len(intervals) - len(res)