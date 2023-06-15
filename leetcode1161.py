# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        res = 0
        g_sum = float('-inf')
        i = 0
        
        q.append(root)
        while q:
            i += 1
            row_sum = 0
            for _ in range(len(q)):
                n = q.popleft()
                row_sum += n.val
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
            if row_sum > g_sum:
                res = i
                g_sum = row_sum
        
        return res

