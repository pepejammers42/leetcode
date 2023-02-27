# 1339. Maximum Product of Splitted Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.subtrees = []
        
        def dfs(n):
            if not n:
                return 0
            l = dfs(n.left)
            r = dfs(n.right)
            
            s = l + r + n.val 
            self.subtrees.append(s)
            return s
        
        total = dfs(root)
        print(self.subtrees)
        print(total)
        r = 0
        for t in self.subtrees:
            r = max(r, t * (total - t))
        return r % (10**9 + 7)
