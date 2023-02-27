# 149. Max Points on a Line

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        result = 1
        
        for i in range(len(points)):
            slopes = defaultdict(int)
            for j in range(i + 1, len(points)):
                x0,y0 = points[i]
                x1,y1 = points[j]
                if x0 == x1:
                    m = float('inf')
                else:
                    m = (y1-y0)/(x1-x0)
                slopes[m] += 1
                result = max(result, slopes[m] + 1)
        return result
