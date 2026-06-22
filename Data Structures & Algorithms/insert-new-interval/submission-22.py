class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals
        for i in range(len(intervals)+1):
            if i == len(intervals) or intervals[i][0] > newInterval[0]:
                break
        if i > 0 and intervals[i-1][1] >= newInterval[0]:
            intervals[i-1][0] = min(intervals[i-1][0], newInterval[0])
            intervals[i-1][1] = max(intervals[i-1][1], newInterval[1])
            i -= 1
        else: intervals.insert(i, newInterval)
        j = i+1
        while j < len(intervals):
            if intervals[j][0] <= intervals[i][1]:
                intervals[i][1] = max(intervals[i][1], intervals[j][1])
                intervals.pop(j)
                j -= 1
            j += 1

        return intervals

        