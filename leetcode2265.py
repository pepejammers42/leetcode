# 2265. Count Nodes Equal to Average of Subtree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        
        def dfs(n):
            if not n:
                return (0,0)
            s= n.val
            cnt = 1
            
            a, b = dfs(n.left)
            c, d = dfs(n.right)
            s = s + a + c
            cnt = cnt + b + d
            
            if (s // cnt) == n.val:
                self.total += 1

            return (s, cnt)
            
        dfs(root)
        return self.total 
