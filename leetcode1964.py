class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        dp = []
        res = []
        
        for o in obstacles:
            ind = bisect_right(dp, o)

            if ind < len(dp):
                dp[ind] = o
            else:
                dp.append(o)
            
            res.append(ind +1)

        return res
