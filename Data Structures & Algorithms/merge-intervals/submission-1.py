class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def isOverlap(a, b):
            a_start, a_end = a[0], a[1]
            b_start, b_end = b[0], b[1]

            if a_start > b_end or b_start > a_end:
                return False
            return True

        def merge(a, b):
            a_start, a_end = a[0], a[1]
            b_start, b_end = b[0], b[1]

            merged_start = min(a_start, b_start)
            merged_end = max(a_end, b_end)
            return [merged_start, merged_end]
        
        intervals.sort(key=lambda x: x[0])
        res = []

        for i in range(len(intervals)):
            # end of the last element is larger or equal than the curretn interval
            if len(res) == 0 or not isOverlap(res[-1], intervals[i]):
                res.append(intervals[i])
            
            else:
                # merge current to the last of res
                last_interval = res.pop()
                res.append(merge(last_interval, intervals[i]))

        return res

                



        