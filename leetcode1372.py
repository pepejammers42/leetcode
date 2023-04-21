# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(root, d, count):
            if not root:
                return count
            
            # prev is right, so +1
            l = dfs(root.left, 0, count+1 if d == 1 else 1)
            # prev is left so +1
            r = dfs(root.right, 1, count+1 if d == 0 else 1)
            
            return max(l,r)
             
        return dfs(root, -1, 0) - 1
