# 797. All Paths From Source to Target
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph) - 1
        
        # [[1,2],[3],[3],[]]
        # 0 -> 1 -> 3
        # 0 -> 2 -> 3
        result = []
        
        def dfs(trav, track):
            nonlocal result

            if trav == n:
                result.append(track[:])
                return
            
            for item in graph[trav]:
                track.append(item)
                dfs(item, track)
                track.pop()
        
        dfs(0, [0])
        
        return result
