# 223. Rectangle Area

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int: 
        area_1 = (ax2-ax1) * (ay2-ay1)
        area_2 = (bx2-bx1) * (by2-by1)
        
        diff = max(min(bx2, ax2) - max(bx1, ax1), 0)  * max(min(by2, ay2) - max(by1, ay1), 0) 
        
        return area_1 + area_2 - max(0, diff)
