class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        intervals.sort(key=lambda x: (x[0], x[1]))
        toAdd, i = 0, 1
        total = 0
        while i < len(intervals):
            while i < len(intervals):
                i1, i2 = intervals[toAdd], intervals[i]
                if i1[0] <= i2[0] and i1[1] >= i2[1]:
                    toAdd = i
                elif not i1[1] > i2[0]:
                    break
                i += 1
            toAdd = i
            total += 1
        return len(intervals) - total