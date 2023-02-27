# 1011. Capacity To Ship Packages Within D Days

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        
        def canShip(v):
            d = 1
            cumulative = 0
            
            for w in weights:
                cumulative += w

                if cumulative > v:
                    d += 1
                    # reset this weight
                    cumulative = w
            return d <= days

        while l < r:
            mid = (l + r) // 2
            
            if canShip(mid):
                r = mid
            else:
                l = mid + 1

        return r

