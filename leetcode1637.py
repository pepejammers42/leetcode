# 1637. Widest Vertical Area Between Two Points Containing No Points

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        p = sorted(points, key=lambda x: x[0])
        r = 0
        
        for i in range(1, len(points)):
            r = max(r, p[i][0]-p[i-1][0])
        return r
