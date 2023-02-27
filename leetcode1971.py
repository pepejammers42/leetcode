# 1971. Find if Path Exists in Graph
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        g = defaultdict(list)
        for s, e in edges:
            g[s].append(e)
            g[e].append(s)
        
        def dfs(start):
            if start == destination:
                return True
            visited.add(start)

            for n in g[start]:
                if n not in visited and dfs(n):
                    return True
            return False

        return dfs(source)
