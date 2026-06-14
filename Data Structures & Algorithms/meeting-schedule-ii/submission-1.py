"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        endIntervals = sorted(intervals, key=lambda x: x.end)
        startIntervals = sorted(intervals, key = lambda x : x.start)

        starts = [x.start for x in startIntervals]
        ends = [x.end for x in endIntervals]

        sP = 0
        eP = 0
        count = 0
        maxCount = 0
        print(starts)
        print(ends)
        while eP < len(ends):
            if sP < len(starts) and starts[sP] < ends[eP]:
                count += 1
                maxCount = max(maxCount, count)
                sP += 1
            else:
                eP += 1
                count -= 1
    
        return maxCount




