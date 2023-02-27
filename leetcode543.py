# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.getH(root)
        return self.ans

    def getH(self, node):
        if not node:
            return 0
        l = self.getH(node.left)
        r = self.getH(node.right)
        
        if l + r > self.ans: self.ans = l + r
        return 1 + max(l, r)