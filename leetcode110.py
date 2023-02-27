#110. Balanced Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def hDiff(node):
            if not node:
                return 0 
            l = hDiff(node.left)
            r = hDiff(node.right)
            
            if l == -1 or r == -1 or abs(l - r) > 1: return -1
            return 1 + max(l, r)

        return hDiff >= 0