# 1137. N-th Tribonacci Number

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        elif n == 1: return 1
        elif n == 2: return 1

        x = 0
        y = 1 
        z = 1

        for _ in range(n - 3):
            x, y, z = y, z, x+y+z
        return z 
