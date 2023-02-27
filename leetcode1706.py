# 1706. Where Will the Ball Fall

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        r = [None for _ in range(len(grid[0]))] 
        for i in range(len(grid[0])):
            curr_x = i
            j = 0
            while j < len(grid):
                if grid[j][curr_x] == 1:
                    if curr_x == len(grid[0]) - 1:
                        break
                    if curr_x + 1 < len(grid[0]) and grid[j][curr_x + 1] == -1:
                        break
                    curr_x += 1
                    j += 1
                    
                elif grid[j][curr_x] == -1:
                    if curr_x == 0:
                        break
                    if curr_x - 1 >= 0 and grid[j][curr_x - 1] == 1:
                        break
                    curr_x -= 1
                    j += 1
                
            if j == len(grid):
                r[i] = curr_x
        return r