# 938. Range Sum of BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.r = 0
        
        def dfs(n):
            if not n:
                return
            if n.val < low:
                dfs(n.right)
            elif n.val > high:
                dfs(n.left)
            else:
                dfs(n.left)
                dfs(n.right)
                self.r += n.val

        dfs(root)
        return self.r
