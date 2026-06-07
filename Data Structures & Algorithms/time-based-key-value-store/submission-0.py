
import bisect
from collections import defaultdict
class TimeMap:

    def __init__(self):
       # hashmap k = key v = [(timestamp, value)] # do binary search on the list by the timestamp
       self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        li = self.timemap[key]
        
        # find the most right index to keep the current order
        insert_idx = bisect.bisect_right(li, timestamp, key=lambda x: x[0], )
        print(insert_idx)
        if insert_idx == len(li):
            return li[-1][1]
        if insert_idx == 0:
            return ""
        return li[insert_idx-1][1]
