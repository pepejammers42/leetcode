# 263. Ugly Number
class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        else:
            while n % 2 == 0: n = n/2
            while n % 3 == 0: n = n/3
            while n % 5 == 0: n = n/5
            return n == 1

