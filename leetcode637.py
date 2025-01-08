# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        res = []
        q = deque([root])

        while q:
            l = len(q)
            total = 0
            for i in range(l):
                tmp = deque.popleft(q)

                if tmp.left:
                    q.append(tmp.left)
                if tmp.right:
                    q.append(tmp.right)
                total += tmp.val
            res.append(total * 1.0 / l * 1.0)

        return res
