class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        a, b = Dsj(n+1), Dsj(n+1)
        res = 0
        
        for t, e1, e2 in edges:
            if t == 3:
                res += a.union(e1, e2)
                b.union(e1, e2)
        
        for t, e1, e2 in edges:
            if t == 1:
                res += a.union(e1, e2)
            if t == 2:
                res += b.union(e1, e2)
        if a.edges == b.edges == n - 1:
            return res
        return -1
            

class Dsj:
    def __init__(self, size):
        self.p = list(range(size))
        self.rank = [0 for _ in range(size)]
        self.edges =  0
    
    def find(self, x):
        if x == self.p[x]:
            return self.p[x]
        # path compression
        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        a = self.find(x)
        b = self.find(y)
        
        if a != b:
            if self.rank[a] < self.rank[b]:
                a, b = b, a
        
            self.p[b] = a
            
            # update rank
            if self.rank[a] == self.rank[b]:
                self.rank[a] = self.rank[b] + 1
            
            self.edges += 1
            return 0
        return 1
