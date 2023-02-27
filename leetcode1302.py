# 1302. Deepest Leaves Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        
        while q:
            curr = q
            q = deque()
            
            for n in curr:
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)

        return sum(x.val for x in curr)
