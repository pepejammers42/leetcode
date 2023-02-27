# 452. Minimum Number of Arrows to Burst Balloons

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        result = 1
        cs, ce = points[0]
        
        for s,e in points[1:]:
            if s > ce:
                result += 1
                cs, ce = s, e
            else:
                ce = min(e, ce)

        return result

