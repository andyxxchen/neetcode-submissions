class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #    i.   j. 
        # [[1,2],[1,4],[2,4],[3,7],[4,9],[6,10]]

        # ===
        # =====================
        #     =================


        # sort the intervals by its start time
        # if overlap, remove the one with bigger end time

        intervals.sort()
        # [[1,2],[1,4],[2,4]]

        remove = 0
        prevEnd = intervals[0][1] # 2

        for start, end in intervals[1:]:
            if start >= prevEnd: # no overlap 
                prevEnd = end
            else:
                # overlap
                remove += 1
                prevEnd = min(end, prevEnd) # preserve the small one, remove the bigger one

        return remove
