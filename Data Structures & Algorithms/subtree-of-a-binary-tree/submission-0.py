# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subRoot_ = subRoot
        
        def isSameTree(p, q):
            if p == None and q != None or p != None and q == None:
                return False
            if not p and not q:
                return True
            if p.val != q.val:
                return False
            
            left_bool = isSameTree(p.left, q.left)
            right_bool = isSameTree(p.right, q.right)

            return left_bool and right_bool

        res = False
        def traverse(node):
            nonlocal res
            if not node:
                return

            if node.val == subRoot.val:
                node_p = node
                if isSameTree(node, subRoot_):
                    res = True
            
            traverse(node.left)
            traverse(node.right)
        
        
        traverse(root)
        return res