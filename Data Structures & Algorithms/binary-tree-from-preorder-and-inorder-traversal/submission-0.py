# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # traverse preorder list 
        # find index in inorder list
        # left half is in left tree 
        # right half is in right tree
        # at the end of the day, we only have left[2] right[3,4]
        # do it to the left sub tree, 
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        # mid is the number of node in left subtree, that's why we count the mid number of node in preorder as well
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root