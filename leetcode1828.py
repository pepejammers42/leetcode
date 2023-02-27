# 1828. Queries on Number of Points Inside a Circle

class Solution(object):
    def countPoints(self, points, queries):
        ans = []
        for i, j, r in queries:
            res = 0
            for x, y in points:
                distance = ((i-x)**2+(j-y)**2)**0.5
                if distance<=r:
                    res+=1
            ans.append(res)
        return ans
