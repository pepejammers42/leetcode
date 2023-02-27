# 542. 01 Matrix

from typing import List
from collections import deque 

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        go = deque()
        N, M = len(mat), len(mat[0])
        visited = set()
        r = [ [-1] * M for _ in range(N)]
        
        for i in range(N):
            for j in range(M):
                if mat[i][j] == 0:
                    go.append((i, j, 0))
                    r[i][j] = 0
        
        while go:
            i, j, cnt = go.popleft()
            if (i, j) in visited:
                continue
            visited.add((i,j))
            
            if r[i][j] == -1:
                r[i][j] = cnt
            
            dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for d in dirs:
                nx, ny = i + d[0], j + d[1]
                if 0 <= nx <= N - 1 and 0 <= ny <= M-1 and (nx,ny) not in visited:
                    go.append((nx, ny, cnt + 1))
        return r
