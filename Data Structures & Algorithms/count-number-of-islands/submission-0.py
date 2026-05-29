class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        # mark 0
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            
            if grid[i][j] == '1':
                grid[i][j] = 0
                # go four direction and clean
                dfs(i-1, j)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i, j+1)
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)

        return res

        