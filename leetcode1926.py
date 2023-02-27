# 1926. Nearest Exit from Entrance in Maze

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        r, c = len(maze), len(maze[0])
        
        for i in range(r):
            for j in range(c):
                if maze[i][j] == '.' and (i == 0 or i == r - 1 or j == 0 or j == c-1): 
                    maze[i][j] = '-'
        maze[entrance[0]][entrance[1]] = 'e'
        
        q = deque()
        q.append((entrance[0], entrance[1]))
        
        res = 0
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]] 
        exited = False
          
        while q:
            for _ in range(len(q)):
                rr, cc = q.popleft()
                for d in dirs:
                    nr, nc = rr + d[0], cc + d[1]
                    if 0 <= nr <= r - 1 and 0 <= nc <= c - 1 and maze[nr][nc] == '-':
                        return res + 1
                    if 0 <= nr <= r - 1 and 0 <= nc <= c - 1 and maze[nr][nc] == '.':
                        maze[nr][nc] = '+'
                        q.append((nr,nc))
            res += 1

        return -1
