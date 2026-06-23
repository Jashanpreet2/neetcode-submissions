import heapq
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        if len(intervals) == 1:
            return 1
        intervals.sort(key=lambda i: i.start)
        curRooms = [intervals[0].end]
        maxRooms = 0
        i=1
        while i < len(intervals):
            while len(curRooms) > 0 and curRooms[0] <= intervals[i].start:
                heapq.heappop(curRooms)
            heapq.heappush(curRooms, intervals[i].end)
            maxRooms = max(maxRooms, len(curRooms))
            i += 1
        return maxRooms