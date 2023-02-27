# 1962. Remove Stones to Minimize the Total
import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        
        for p in piles:
            heapq.heappush(heap, -p)
        
        for _ in range(k):
            tmp = -1*heapq.heappop(heap)
            heapq.heappush(heap, -math.ceil(tmp/2))

        return -sum(heap) 
