class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        vis = set()
        res = 0
        def dfs(i):
            if i in vis:
                return 0
            vis.add(i)
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    dfs(j)
            return 1
        
        for i in range(len(isConnected)):
            res += dfs(i)
        return res