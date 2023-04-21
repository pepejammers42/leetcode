# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([[root, 1]])
        wid = 0

        while q:
            # go through one level at a time
            l, r = q[0][1], q[-1][1]
            wid = max(wid, r-l+1)
            
            next_level = deque()
            while q:
                curr = q.popleft()
                if curr[0].left:
                    next_level.append([curr[0].left, curr[1] * 2])
                if curr[0].right:
                    next_level.append([curr[0].right, curr[1] * 2 + 1])
            q = next_level 

        return wid 
