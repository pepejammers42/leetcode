class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        
        def dfs(cur, total, i):
            if total > target:
                return
            if total == target:
                res.append(cur)
            
            for j in range(i, n):
                dfs(cur + [candidates[j]], total + candidates[j], j)
        
        dfs([], 0, 0)
        return res