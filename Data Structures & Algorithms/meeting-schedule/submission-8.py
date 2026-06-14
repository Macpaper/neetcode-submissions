"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals or len(intervals) == 1: return True
        intervals.sort(key = lambda r : r.start)
        shifts = [intervals[0]]

        for i in intervals[1:]:
            prevEnd = shifts[-1].end
            print("previous start: ", )
            if i.start < prevEnd:
                return False
            else:
                shifts.append(i)
        return True