# 587. Erect the Fence

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        return self.graham_scan(trees)
        
    def check_dir(self, a,b,c):
        check = (c[1] - b[1])*(b[0] - a[0]) - (c[0] - b[0])*(b[1] - a[1])
        if check < 0:
            return -1
        elif check > 0: 
            return 1
        else:
            return 0
    
    def dist(self, a,b):
        return math.sqrt((b[1] - a[1])**2 + (b[0] - a[0])** 2) 

    def p_angles(self, a, b):
        if a[1] == b[1]: return -math.pi
        return math.atan2(b[1]-a[1], b[0]-a[0])
    
    def col(self, a, b, c):
        c = a[0]*(b[1]-c[1]) + b[0]*(c[1] - a[1]) + c[0]*(a[1] - b[1])
        return 1 if c == 0 else 0

    def graham_scan(self, points):
        # find min y, if duplicates, find with min x
        min_p = min(points, key=lambda p: (p[1], p[0]))
        # sort by angle.
        points.sort(key=lambda p: (self.p_angles(min_p, p), self.dist(min_p, p)))
        hull = []
        visited = set()
        
        for i in range(len(points)):
            while len(hull) >= 2 and self.check_dir(hull[-2], hull[-1], points[i]) == -1:
                t = hull.pop()
                visited.remove(tuple(t))
            hull.append(points[i])
            visited.add(tuple(points[i]))
            
        # check collinear points between the last one checked and the center. 
        if len(points) > 3:
            for i in range(len(points) - 2, 0, -1):
                if tuple(points[i]) not in visited and self.col(points[0], points[-1], points[i]) == 1:
                    visited.add(tuple(points[i]))
                    hull.append(points[i])
        return hull
