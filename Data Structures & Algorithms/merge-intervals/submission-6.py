class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x)
        print(intervals)
        res = []
        i = 0
        while i < len(intervals):
            maxEnd = intervals[i][1]
            j = i
            i += 1
            while i < len(intervals) and (intervals[i][0] == intervals[j][0] or intervals[i][0] <= maxEnd):
                maxEnd = max(maxEnd, intervals[i][1])
                intervals[i] = None
                i += 1
            intervals[j][1] = maxEnd
        for interval in intervals:
            if interval is not None:
                res.append(interval)
        return res