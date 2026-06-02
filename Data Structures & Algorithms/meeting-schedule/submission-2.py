"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        def isOverlap(a, b):
            a_start, a_end = a.start, a.end
            b_start, b_end = b.start, b.end

            if b_start >= a_end or a_start >= b_end:
                return False
            return True

        for i in range(0, len(intervals)-1):
            if isOverlap(intervals[i], intervals[i+1]):
                return False
        return True
        
        