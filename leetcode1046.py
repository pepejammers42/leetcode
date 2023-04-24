class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        t = []
        for s in stones:
            heapq.heappush(t, -s)
        
        while len(t) > 1:
            t1, t2 = -heapq.heappop(t), -heapq.heappop(t)
            if t1 != t2:
                heapq.heappush(t, -t1 + t2)
        
        if len(t) == 1:
            return -t[0]
        return 0
