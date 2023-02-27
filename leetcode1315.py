# 1315. Sum of Nodes with Even-Valued Grandparent

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.total = 0
        
        def dfs(n):
            if not n:
                return
            if n.val %2 == 0:
                if n.left:
                    if n.left.left: self.total += n.left.left.val
                    if n.left.right: self.total += n.left.right.val
                if n.right:
                    if n.right.left: self.total += n.right.left.val
                    if n.right.right: self.total += n.right.right.val
                    
            dfs(n.left)
            dfs(n.right)
        
        dfs(root)
        return self.total
