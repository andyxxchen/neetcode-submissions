# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    level order traversal, get the last element of each layer
'''
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []

        while q:
            size = len(q)
            for i in range(size):
                cur_node = q.popleft()
                if i == size - 1: # last element
                    res.append(cur_node.val)
                
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
                
        return res