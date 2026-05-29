# a valid tree should have exactly n-1 edges
# a valid tree shouldn't have any loop
# all node should be connected to each other, start form one can dfs to all others

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1


# union find
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)

        if len(edges) != n-1:
            return False

        for u, v in edges:
            uf.union(u, v)
        
        for i in range(1, n):
            if uf.find(i) != uf.find(i-1):
                return False
        
        return True
