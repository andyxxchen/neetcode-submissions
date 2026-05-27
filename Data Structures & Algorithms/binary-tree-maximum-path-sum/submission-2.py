# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            left_gain = dfs(node.left)
            right_gain = dfs(node.right)
            
            cur_val = node.val + left_gain + right_gain
            cur_path = node.val + max(left_gain, right_gain)
            res = max(res, cur_val)
            if cur_val < 0:
                return 0
            return cur_path
        dfs(root)
        return res

