'''                                 i=1
    intervals = [[1,3],[4,6],[7,9],[11,12]]
    newInterval = [4,9]
    res = [[1,3]]

    1. traverse interlvals 
        if new_start < end:
            # start insertion 
            new_Interval[0] = min(interval[0], new_Interval[0])
    
    2. keep traversing if start of interval j <= new_interval end
    
    3. j -= 1
    4. new_interval[1] = max(interval[j][1], new_interval[2])

    insert the rest of the elements
'''


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)

        if not intervals:
            return [newInterval]
        res = []

        def isOverlap(intervalA, intervalB ):
            a_start, a_end = intervalA[0],intervalA[1]
            b_start, b_end = intervalB[0],intervalB[1]

            if b_end < a_start or b_start > a_end:
                return False
            return True
        
        def merge(intervalA, intervalB):
            a_start, a_end = intervalA[0],intervalA[1]
            b_start, b_end = intervalB[0],intervalB[1]
            
            new_start, new_end = min(a_start, b_start), max(a_end, b_end)
                
            return [new_start, new_end]

        cur_interval = newInterval
        i = 0
        while i < n and not isOverlap(cur_interval, intervals[i]) and intervals[i][0] <= cur_interval[0] :
            res.append(intervals[i])
            i += 1
        print(i)
        while i < n and isOverlap(cur_interval, intervals[i]):
            cur_interval = merge(cur_interval, intervals[i])
            i += 1

        print()
        res.append(cur_interval)

        while i < n:
            res.append(intervals[i])
            i += 1

        return res

