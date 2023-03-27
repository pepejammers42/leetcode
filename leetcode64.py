# 64. Minimum Path Sum

from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = []

        cnt = 0
        for i in range(m):
            dp.append([grid[i][0] + cnt])
            cnt += grid[i][0]
        
        for j in range(1,n):
            dp[0].append(grid[0][j]+dp[0][j-1])
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i].append((grid[i][j] + min(dp[i-1][j], dp[i][j-1])))

        return dp[-1][-1]
