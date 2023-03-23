# Leetcode 365: Water Jug Problem

from typing import Deque


class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        q = Deque()
        vis = set()
        
        q.append(0)
        vis.add(0)
        
        while q:
            trav = q.popleft()
            
            for op in [-jug1Capacity, jug1Capacity, -jug2Capacity, jug2Capacity]:
                curr = trav + op
                
                if curr == targetCapacity: return True
                if curr < 0 or curr > jug1Capacity + jug2Capacity: continue
                if curr not in vis:
                    q.append(curr)
                    vis.add(curr)
    
        return False
