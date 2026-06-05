'''
    Window position            Max
    ---------------           -----
     l        r
    [1  2  1] 0  4  2  6        2
    1 [2  1  0] 4  2  6        2
    1  2 [1  0  4] 2  6        4
    1  2  1 [0  4  2] 6        4
    1  2  1  0 [4  2  6]       6

    heapq  = len of k
    
    window 
    remove left = nums[r - k]
    add r right = nums[r]
    to 
    freq {
        1: 2
        2: 1
    }
        if the removed one is == cur_max and freq[cur_max] == 0:
            cur -> next maximum value in the maxheap
        else: 
            push into the maxheap

    cur_max = max(cur_max, r)
    res.append(cur_max)



2.
    inside of heap, we store (-value, index)
    we don't care if current heap oversized, but we do care each time we try to add the max value, it's within the right window (valid index > i - k < i )

'''

# maxheap, store negative value
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))

            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                output.append(-heap[0][0])
        
        return output
            