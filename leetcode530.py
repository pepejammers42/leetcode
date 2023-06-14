# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def dfs(n):
            if n is None:
                return []
            return dfs(n.left) + [n.val] + dfs(n.right)
        
        l = dfs(root)
        res = float('inf')
        for i in range(1, len(l)):
            res = min(res, l[i]-l[i-1])
        return res