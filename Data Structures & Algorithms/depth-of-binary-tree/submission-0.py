# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(node, cur_depth): 
            if not node: 
                return cur_depth
            cur_depth += 1

            left_depth = dfs(node.left, cur_depth)
            right_depth = dfs(node.right, cur_depth)
            

            
            return max(left_depth, right_depth)
        
        depth = 0
        res = dfs(root, depth)
        return res
            

            
