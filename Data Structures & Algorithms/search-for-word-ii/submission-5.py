class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build Tries
        
        for word in words:
            node = self.root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = word
        
        res = []
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        
        def out_of_range(i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return True
            return False

        def dfs(i, j, node, visited):
            if node.word:
                res.append(node.word)
                node.word = None # key point
            
            candidates = []
            for dx, dy in dirs:
                if (i+dx, j+dy) in visited or out_of_range(i+dx, j+dy):
                    continue
                ch = board[i+dx][j+dy]
                if ch not in node.children:
                    continue
                
                visited.add((i+dx, j+dy))
                dfs(i+dx, j+dy, node.children[ch], visited)
                visited.remove((i+dx, j+dy))
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in self.root.children:
                    dfs(i, j, self.root.children[board[i][j]], {(i, j)})
        return res