'''
    everytime we call add() it will add a val into the array, and return the kth largest

    heap with size of k
    max_heap
'''
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = nums
        heapq.heapify(self.pq)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)
        val = heapq.nlargest(self.k, self.pq)
        
        return val[-1]