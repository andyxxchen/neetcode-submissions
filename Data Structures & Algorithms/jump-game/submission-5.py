
# 1. BFS
# 2. DFS O()

from collections import deque
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        visited = [False] * n

        def dfs(i): # at index i
            if i >= len(nums) or visited[i] == True:
                return
            
            visited[i] = True
            for offset in range(nums[i],0,-1):
                dfs(i + offset)

        dfs(0)
        return visited[-1]

        
    
