# 1833. Maximum Ice Cream Bars

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        result = 0
        costs.sort()
        for c in costs:
            if c <= coins:
                coins -= c
                result += 1
            else:
                break
        return result
