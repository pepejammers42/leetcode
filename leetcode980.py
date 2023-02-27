# 980. Unique Paths III
from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        result = 0
        M, N = len(grid), len(grid[0])
        whites = 0
        start = None
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    start = (i,j)
                if grid[i][j] == 0:
                    whites += 1
        
        def dfs(posr, posc, whites):
            nonlocal result
            grid[posr][posc] = -2 #visited
            for rr, cc in [(0,1),(0,-1),(-1,0),(1,0)]:
                r, c = posr + rr, posc + cc
                if 0<= r < M and 0 <= c < N:
                    if grid[r][c] == 0:
                        dfs(r, c, whites -1)
                    if grid[r][c] == 2 and whites == 0:
                        result += 1
            grid[posr][posc] = 0
            
        dfs(*start, whites)

        return result
