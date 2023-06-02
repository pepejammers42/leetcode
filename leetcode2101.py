class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        g = defaultdict(list)
        
        for b1 in range(len(bombs)):
            a,b,c = bombs[b1]
            for b2 in range(b1 + 1, len(bombs)):
                d,e,f = bombs[b2]
                dis = sqrt((d-a)**2 + (e-b)**2)
                
                if dis <= c:
                    g[b1].append(b2)
                if dis <= f:
                    g[b2].append(b1)

        def dfs(i, visited):
            if i in visited:
                return 0
            visited.add(i)
            for n in g[i]:
                dfs(n, visited)
            return len(visited)
        
        res = 0
        for i in range(len(bombs)):
            res = max(res, dfs(i, set()))

        return res