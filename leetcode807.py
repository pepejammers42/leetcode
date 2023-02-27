# 807. Max Increase to Keep City Skyline

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        inc = 0
        mr, mc = [0 for _ in range(len(grid))], [0 for _ in range(len(grid[0]))] 

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                mr[x] = max(mr[x], grid[x][y])
                mc[y] = max(mc[y], grid[x][y])
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                inc += min(mr[x], mc[y]) - grid[x][y]
        
        return inc
