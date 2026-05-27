# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(p, q):
            if p == None and q != None or p != None and q == None:
                return False
            if not p and not q:
                return True
            if p.val != q.val:
                return False
            
            left_bool = dfs(p.left, q.left)
            right_bool = dfs(p.right, q.right)

            return left_bool and right_bool

        return dfs(p, q)