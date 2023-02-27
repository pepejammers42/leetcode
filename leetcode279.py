# 279. Perfect Squares

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n for _ in range(n + 1)]  
        dp[0] = 0
        
        sq = [x**2 for x in range(0, n) if x**2<=n]
        
        for i in range(len(dp)):
            for s in sq:
                if s > i: break
                dp[i] = min(dp[i], 1 + dp[i - s])
        return dp[-1]
