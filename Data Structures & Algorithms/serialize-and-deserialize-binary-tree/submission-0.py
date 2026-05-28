# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # [12NN34NN5NN]
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            nonlocal res
            if not node:
                res.append("N")
                return
            res.append(str(node.val)) # [1, 12] etc..
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    # [12NN34NN5NN] -> build tree
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data_array = data.split(',')
        if not data_array:
            return None
        idx = 0

        def dfs() -> TreeNode:
            nonlocal idx
            if data_array[idx] == 'N':
                idx += 1
                return None

            node = TreeNode(val=data_array[idx])
            idx += 1
            node.left = dfs()
            node.right = dfs()
            return node
            
        root = dfs()
        return root