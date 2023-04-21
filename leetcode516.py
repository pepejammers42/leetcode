class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1 = s[::-1] 
        N, M = len(s), len(s1)
        dp = [ [0] * (M+1) for _ in range(N+1)]
        
        for i in range(N):
            for j in range(M):
                if s[i] == s1[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        
        return dp[-1][-1]
        
