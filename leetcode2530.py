# 2530. Maximal Score After Applying K Operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        score = 0
        
        for n in nums:
            heapq.heappush(heap, -n)
        
        for _ in range(k):
            tmp = -heapq.heappop(heap)
            score += tmp
            heapq.heappush(heap, -math.ceil(tmp/3))
        return score
