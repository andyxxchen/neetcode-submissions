"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

'''
    we regard start[s] as the current time
    every time we get a new start[s], means we encounter a new meeting
    room = 1
    2 possibilities
        1. start[i] >= end[e]
            we can free meeting rooms
            move end to the next one, until we got a larger end time:
                free 1

        2. start[i] < end[e]:
            meeting += += 1

    1
'''

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # [(0,40),(5,10),(15,20)]
        # start = [0, 5, 15]
        # end = [10, 20, 40]

        start =[]
        end = []
        for interval in intervals:
            start.append(interval.start) 
            end.append(interval.end)
        
        start.sort()
        end.sort()

        s = 0
        e = 0
        room = 0
        res = 0
        while s < len(intervals) and e < len(intervals):
            if start[s] >= end[e]:
                e += 1
                room -= 1
                while e < len(intervals) and end[e-1] == end[e]:
                    room -= 1
                    e += 1
            else:
                room += 1
                res = max(res, room)
                s += 1

        return res