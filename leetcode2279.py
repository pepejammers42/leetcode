# 2279. Maximum Bags With Full Capacity of Rocks

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        result = 0
        gap = []
        
        for i in range(len(capacity)):
            gap.append(capacity[i] - rocks[i])
        
        gap.sort()
        
        for g in gap:
            if additionalRocks >= g:
                additionalRocks -= g
                result += 1
            else:
                break
        
        return result
