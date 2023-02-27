# 1834. Single-Threaded CPU

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        result = []
        lineup = sorted([k + [i] for i,k in enumerate(tasks)])
        
        minheap = []
        i = 0
        time = lineup[0][0]
        
        while minheap or i < len(lineup):
            while i < len(lineup) and time >= lineup[i][0]:
                heapq.heappush(minheap, (lineup[i][1], lineup[i][2]))
                i += 1
            
            if not minheap:
                time = lineup[i][0]
            else:
                process, pos = heapq.heappop(minheap)
                time += process
                result.append(pos)

        return result
