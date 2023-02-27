# 790. Domino and Tromino Tiling

class Solution:
    def numTilings(self, n: int) -> int:
        dp = [0] * 1001
        dp[0] = 1
        dp[1] = 2
        dp[2] = 5
        md = 1000000007
        if n <= 3:
            return dp[n-1]
        for i in range(4, n):
            dp[i] = 2*dp[i-1] + dp[i-3]
        return dp[n] % md
