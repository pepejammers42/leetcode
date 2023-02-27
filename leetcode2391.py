# 2391. Minimum Amount of Time to Collect Garbage

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        r = 0
        dist = [0] * len(garbage)
        to_col = [0] * 3
        gar = 0
        
        def get_ind(s):
            for i in range(len(garbage)-1, -1, -1):
                if s in garbage[i]:
                    return i
            return 0

        for i in range(len(garbage)):
            gar += len(garbage[i])
            
            to_col[0] = get_ind('G')
            to_col[1] = get_ind('P')
            to_col[2] = get_ind('M')
            
            if i > 0:
                dist[i] = dist[i-1] + travel[i-1]
        
        for t in to_col:
            r += dist[t]
        return r + gar
