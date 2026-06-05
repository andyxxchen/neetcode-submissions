class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])

        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(i, j):
            if 0 > i or i >= len(grid) or 0 > j or j >= len(grid[0]) or grid[i][j] != 1:
                return
            
            nonlocal cur, res
            
            cur += 1
            grid[i][j] = 0
            res = max(res, cur)
            for dx, dy in dirs:
                dfs(i+dx, j+dy)
        

        for i in range(m):
            for j in range(n):
                cur = 0
                dfs(i, j)

        return res