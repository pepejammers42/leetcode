class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for _ in range(n)] 
        cnt = 0
        a, b, c, d = 0, 0, n, n
        
        while a < c or b < d:
            for i in range(b, d):
                cnt += 1
                res[a][i] = cnt
            a += 1
            for i in range(a, c):
                cnt += 1
                res[i][d-1] = cnt
            d -= 1
            for i in range(d-1, b-1, -1):
                cnt += 1
                res[c-1][i] = cnt
            c -= 1
            for i in range(c-1, a-1, -1):
                cnt += 1
                res[i][b] = cnt
            b += 1

        return res