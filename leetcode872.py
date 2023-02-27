# 872. Leaf-Similar Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(n, l):
            if n:
                if not n.left and not n.right:
                    l += [n.val]
                dfs(n.left, l)
                dfs(n.right, l) 
            return l
        
        return dfs(root1, []) == dfs(root2, [])
