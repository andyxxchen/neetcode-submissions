'''
    choose the heaviest two stone, use a maxHeap
'''
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-x for x in stones]
            
        heapq.heapify(pq)

        while len(pq) > 1:
            stone1 = - heapq.heappop(pq)
            stone2 = - heapq.heappop(pq)

            stone1 = stone1 - stone2 if stone1 > stone2 else 0
            if stone1 != 0:
                heapq.heappush(pq, -stone1)
        
        return -pq[0] if pq else 0

