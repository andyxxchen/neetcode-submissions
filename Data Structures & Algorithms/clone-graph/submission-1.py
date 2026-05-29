"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node_):
            if node_ in oldToNew:
                return oldToNew[node_]

            cur_node = Node(val=node_.val)
            oldToNew[node_] = cur_node
            for item in node_.neighbors:
                cur_node.neighbors.append(dfs(item))

            return cur_node

        return dfs(node) if node else None