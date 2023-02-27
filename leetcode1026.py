# 1026. Maximum Difference Between Node and Ancestor

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.r = 0
        
        def dfs(n, ma, mi):
            if not n:
                return
            ma = max(n.val, ma)
            mi = min(n.val, mi)

            self.r = max(self.r, abs(ma-mi))
            dfs(n.left, ma, mi)
            dfs(n.right, ma, mi)
            
        dfs(root, root.val, root.val)
        return self.r 
