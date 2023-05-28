class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
    
        @lru_cache(None)
        def dfs(l,r):
            # if len 1 then u can't cut then the cost is 0
            if r - l == 1:
                return 0
            
            res = float('inf')
            for c in cuts:
                if l < c < r:
                    res = min(res, (r-l) + dfs(l, c) + dfs(c, r))
            
            return res if res != float('inf') else 0
        
        return dfs(0, n)