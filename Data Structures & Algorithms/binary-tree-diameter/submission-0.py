# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        # return left and right height
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            cur_height = max(left+1, right+1)
            res = max(res, left + right)

            return cur_height

        dfs(root)
        return res