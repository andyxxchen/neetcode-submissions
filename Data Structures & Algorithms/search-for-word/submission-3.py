class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        dir = [(0,1), (1,0), (-1,0), (0,-1)]
        
        def dfs(i, j, visited, k):
            nonlocal res
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                # out of index
                return

            if k == len(word)-1:
                res = True
                return
        
            for dx, dy in dir:
                if (i+dx, j+dy) in visited:
                    continue
                
                if i+dx < 0 or j+dy < 0 or i+dx >= len(board) or j+dy >= len(board[0]):
                # out of index
                    continue
                
                if word[k+1] == board[i+dx][j+dy]:
                    visited.add((i+dx, j+dy))
                    dfs(i+dx, j+dy, visited, k+1)
                    visited.remove((i+dx, j+dy))
            
            return

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    dfs(x,y, {(x,y)},0)
        return res