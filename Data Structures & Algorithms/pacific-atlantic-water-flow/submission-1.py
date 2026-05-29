class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [(0,1),(0,-1),(-1,0),(1,0)]        
        m = len(heights)        
        n = len(heights[0])

        # if it can flow to Pacific or Atlantic
        def dfs(i, j, canFlow, visited):
            # if top right corner or bottom left corner
            if (i, j) == (m-1, 0) or (i, j) == (0, n-1):
                canFlow[0] = True
                canFlow[1] = True
                return
            if i == 0 or j == 0:
                canFlow[0] = True
                # canFlow[1] = False

            if i == m-1 or j == n-1:
                # canFlow[0] = False
                canFlow[1] = True

            visited.add((i,j))

            for dx, dy in dirs:
                x = i+dx
                y = j+dy
                if x < 0 or y < 0 or x >= m or y >= n:
                    continue

                # if there are two equal, it might leads to infinity loop
                if heights[i][j] >= heights[x][y] and (x,y) not in visited:
                    # can flow
                    dfs(x, y, canFlow, visited)
                
            return


        res = []        
        for i in range(m):
            for j in range(n):
                PA = [False, False]
                dfs(i, j, PA, set())
                if PA[0] == True and PA[1] == True:
                    res.append([i, j])

        return res
        
                
                
            
            