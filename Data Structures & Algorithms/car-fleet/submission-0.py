class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # iterative first
        pos_time = []

        for i in range(len(position)):
            pos_time.append((position[i], (target-position[i]) / speed[i]))

        pos_time.sort() # sort by position

        res = 0
        last_time = 0
        # traverse from right to left
        for i in range(len(position) - 1, -1, -1):
            cur_time = pos_time[i][1]
            if cur_time <= last_time:
                continue
            else:
                res += 1
                last_time = cur_time
        
        return res


        