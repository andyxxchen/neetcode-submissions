
# 1. BFS
# 2. DFS visited -> O(n^2)

from collections import deque
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # DFS O(n^2)
        # n = len(nums)
        # visited = [False] * n

        # def dfs(i): # at index i
        #     if i >= len(nums) or visited[i] == True:
        #         return
            
        #     visited[i] = True
        #     for offset in range(nums[i],0,-1):
        #         dfs(i + offset)

        # dfs(0)
        # return visited[-1]

        # BFS O()
        n = len(nums)
        deq = deque([0])
        visited = set()

        while deq:
            cur_idx = deq.popleft()

            if cur_idx in visited or cur_idx >= n:
                continue

            if cur_idx == n-1:
                return True
            
            visited.add(cur_idx)
            for offset in range(1,nums[cur_idx]+1):
                nxt = cur_idx + offset
                deq.append(nxt)

        return False
            

