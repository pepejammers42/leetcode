# 1038. Binary Search Tree to Greater Sum Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.s = 0
        
        def dfs(n):
            if not n:
                return
            dfs(n.right)
            n.val += self.s
            self.s = n.val
            dfs(n.left)

        dfs(root)
        return root
