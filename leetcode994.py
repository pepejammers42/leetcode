# 994. Rotting Oranges

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        x, y = len(grid[0]), len(grid)
        ones = set()
        
        for i in range(y):
            for j in range(x):
                if grid[i][j] == 2:
                    q.append((i,j))
                    grid[i][j] = 0
                if grid[i][j] == 1:
                    ones.add((i,j))
        if not q and not ones:
            return -1
        # bfs
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        time = 0
        while q:
            time += 1
            for _ in range(len(q)):
                p = q.popleft()
                for d in dirs:
                    nx, ny = p[1] + d[0], p[0] + d[1]
                    if 0 <= nx <= x-1 and 0 <= ny <= y-1 and grid[ny][nx] == 1:
                        q.append((ny,nx))
                        grid[ny][nx] = 0
        for i in range(y):
            for j in range(x):
                if grid[i][j] == 1:
                    return -1
        return time - 1
                    
        