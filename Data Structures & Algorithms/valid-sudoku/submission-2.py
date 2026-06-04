class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def checkRow(i):
            s = set()
            for j in range(len(board[0])):
                if board[i][j] in s:
                    print(1)
                    return False
                if board[i][j].isdigit() == True:
                    s.add(board[i][j])
            return True
        
                
        def checkCol(j):
            s = set()
            for i in range(len(board)):
                if board[i][j] in s:
                    print(2)
                    return False
                if board[i][j].isdigit() == True:
                    s.add(board[i][j])
            return True
        
        def check9x9(i,j):
            s = set()
            for r in range(i, i+3):
                for c in range(j, j+3):
                    print(board[r][c])
                    print(s)
                    if board[r][c] in s:
                        print(r,c)
                        print(3)
                        return False
                    if board[r][c].isdigit() == True:
                        s.add(board[r][c])
            return True

        # 0,0. 0,3. 0,6
        # 3,0, 3,3
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i % 3 == 0 and j%3==0 and  (i + j) % 3 == 0:
                    if not check9x9(i,j):
                        return False
                
                if not checkRow(i) or not checkCol(j):
                    return False

        return True