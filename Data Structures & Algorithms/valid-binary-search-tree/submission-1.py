# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True
        def valid(node, minn, maxx): 
            nonlocal res
            if not res or not node:
                return 

            if not(minn < node.val < maxx):
                res = False

            valid(node.left, minn, node.val)
            valid(node.right, node.val, maxx)

        valid(root, float('-inf'), float('inf'))
        return res