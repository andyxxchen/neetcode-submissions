
# we keep two even nums of heap, 1 min heap and 1 max heap
# every time we have a new value from the data stream
# if num > min heap.top()? 
#       insert to minheap
# otherwise insert to maxheap()
#       
# if len(min) - len(max) > 1:
#           rebalance these two heaps
#               1. pop from the larger one
#               2. insert to the smaller one
# To get mid element
# if len(min) == len(max): pop from both and calculate the average of them
# else: pop the larger one

import heapq
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == 0 or num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else: # insert into the maxheap
            heapq.heappush(self.maxHeap, -num)
        
        if abs(len(self.minHeap) - len(self.maxHeap)) > 1:
            # rebalance for even distribution
            if len(self.minHeap) > len(self.maxHeap):
                tmp = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -tmp)
            else:
                tmp = -heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, tmp)

        print(self.minHeap)
        print(self.maxHeap)

    def findMedian(self) -> float:
        mi_sz = len(self.minHeap)
        ma_sz = len(self.maxHeap)
        if mi_sz == ma_sz:
            if mi_sz == 0:
                return 0
            a = self.minHeap[0]
            b = -self.maxHeap[0]
            return (a+b)/2
        else:
            if mi_sz > ma_sz:
                return self.minHeap[0]
            else:
                return -self.maxHeap[0]