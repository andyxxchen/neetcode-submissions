# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traverse, everytime we visit a node we minus 1 to the k
        # if k == 0, the value should be the target
        res = root.val
        def inorder(node):
            nonlocal k, res
            if not node:
                return
            
            inorder(node.left)
            # visit node
            k -= 1
            if k == 0: 
                res = node.val
                return
            inorder(node.right)

        inorder(root)
        return res
