class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        res = 0
        
        ## BRUTE FORCE ##
        
        # for i in range(len(grid)):
        #     for j in range(len(grid)):
        #         isTrue = True
        #         for k in range(len(grid)):
        #             if grid[i][k] != grid[k][j]:
        #                 isTrue = False
        #                 break
        #         if isTrue:
        #             res += 1
                
        cnt = Counter(tuple(r) for r in grid)
        
        for col in zip(*grid):
            res += cnt[col]
        
        return res