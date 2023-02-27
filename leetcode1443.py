# 1443. Minimum Time to Collect All Apples in a Tree

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        paths = defaultdict(list)
        for e1, e2 in edges:
            paths[e1].append(e2)
            paths[e2].append(e1)
        
        def dfs(node, prev):
            result = 0

            for p in paths[node]:
                if p != prev:
                    result += dfs(p, node)
            
            if result > 0 or hasApple[node]:
                return result + 2

            return result

        return max(0, dfs(0, -1)-2)
