class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return
        
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else: # attach y to the x, add 1 to the rank of x
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
                
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) # 1 redundant edge so num of edges is equal to num of vertices
        uf = UnionFind(n)
        
        i = 0
        while i < n:
            a = edges[i][0]
            b = edges[i][1]

            if uf.find(a-1) == uf.find(b-1): # they are already connected, this is the redundant edge
                return edges[i]
            uf.union(a-1, b-1)
            i += 1

        return []
