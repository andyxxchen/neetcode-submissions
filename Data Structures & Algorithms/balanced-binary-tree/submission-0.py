# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    in each recursion, check if the left and right child height gap is more than 1

'''
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(node):
            nonlocal res
            if not res or not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if abs(right - left) > 1:
                res = False
            
            cur_height = max(left+1, right+1)
            return cur_height
        
        dfs(root)
        return res
            
